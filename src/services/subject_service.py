import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

from dao.db_config import supabase

class SubjectService:
    @staticmethod
    def add_subject(name):
        data = {"name": name}
        supabase.table("subject").insert(data).execute()
        print("Subject added successfully!")

    @staticmethod
    def list_subjects():
        subjects = supabase.table("subject").select("*").execute()
        if subjects.data:
            for s in subjects.data:
                print(f"{s['subject_id']} - {s['name']}")
        else:
            print("No subjects found.")
