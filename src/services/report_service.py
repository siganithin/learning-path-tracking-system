import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.db_config import supabase

class ReportService:
    @staticmethod
    def generate_report(plan_id):
        # Fetch tasks for the study plan
        tasks = supabase.table("task").select("*").eq("plan_id", plan_id).execute()
        if not tasks.data:
            print("No tasks found for this plan.")
            return

        total = len(tasks.data)
        completed = len([t for t in tasks.data if t["status"] == "Completed"])
        pending = total - completed
        summary = f"Total Tasks: {total}, Completed: {completed}, Pending: {pending}"

        # Insert report into database
        supabase.table("report").insert({"plan_id": plan_id, "summary": summary}).execute()
        print("Report generated successfully!")
        print(summary)

    @staticmethod
    def view_report(plan_id=None):
        query = supabase.table("report").select("*")
        if plan_id:
            query = query.eq("plan_id", plan_id)
        reports = query.execute()
        if reports.data:
            for r in reports.data:
                print(f"Report ID: {r['report_id']}, Plan ID: {r['plan_id']}, Summary: {r['summary']}")
        else:
            print("No reports found.")
