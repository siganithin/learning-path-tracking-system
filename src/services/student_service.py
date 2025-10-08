<<<<<<< HEAD
from dao.db_config import supabase

class StudentService:
    @staticmethod
    def add_student(name, email):
        data = {"name": name, "email": email}
        supabase.table("student").insert(data).execute()
        print("Student added successfully!")
        
    @staticmethod
    def list_students():
        result = supabase.table("student").select("*").execute()
        return result.data if result.data else []
    
    @staticmethod
    def delete_student(student_id):
        supabase.table("student").delete().eq("student_id", student_id).execute()
        print(f"Student {student_id} deleted.")

=======
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
>>>>>>> 43fa1d364497bf14423a758edbaafb358bec959f
