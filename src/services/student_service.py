from dao.db_config import supabase

class StudentService:
    @staticmethod
    def add_student(name, email):
        if not name or not email:
            raise ValueError("Name and email must not be empty.")
        try:
            data = {"name": name, "email": email}
            result = supabase.table("student").insert(data).execute()
            if not result or result.data is None:
                raise Exception("Failed to insert student.")
            print("Student added successfully!")
        except Exception as e:
            print(f"Failed to add student: {e}")
            raise e

    @staticmethod
    def list_students():
        try:
            result = supabase.table("student").select("*").execute()
            if not result or result.data is None:
                raise Exception("Failed to retrieve students.")
            return result.data
        except Exception as e:
            print(f"Failed to list students: {e}")
            return []

    @staticmethod
    def delete_student(student_id):
        try:
            result = supabase.table("student").delete().eq("student_id", student_id).execute()
            if not result or result.data is None:
                raise Exception("Failed to delete student.")
            print(f"Student {student_id} deleted.")
        except Exception as e:
            print(f"Failed to delete student: {e}")
            raise e
