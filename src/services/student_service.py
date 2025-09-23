from dao.db_config import supabase

class StudentService:
    @staticmethod
    def add_student(name, email):
        data = {"name": name, "email": email}
        supabase.table("student").insert(data).execute()
        print("Student added successfully!")

    @staticmethod
    def list_students():
        students = supabase.table("student").select("*").execute()
        for s in students.data:
            print(f"{s['student_id']} - {s['name']} - {s['email']}")
