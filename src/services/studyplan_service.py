import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

from dao.db_config import supabase

class StudyPlanService:
    @staticmethod
    def create_studyplan(title, student_id, subject_id):
        data = {
            "title": title,
            "student_id": student_id,
            "subject_id": subject_id
        }       
        supabase.table("studyplan").insert(data).execute()
        print("Study plan created successfully!")

    @staticmethod
    def list_studyplans(student_id=None):
        query = supabase.table("studyplan").select("*")
        if student_id:
            query = query.eq("student_id", student_id)
        plans = query.execute()
        return plans.data if plans.data else []
    @staticmethod
    def delete_studyplan(plan_id):
        supabase.table("studyplan").delete().eq("plan_id", plan_id).execute()
        print(f"Study Plan {plan_id} deleted.")

