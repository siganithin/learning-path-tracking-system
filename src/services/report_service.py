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
        data = reports.data if reports.data else []

    # Deduplicate and aggregate by report_id (example)
        unique_reports = {}
        for r in data:
            rid = r["report_id"]
            if rid not in unique_reports:
            # You might want to adjust summary aggregation etc. here
                unique_reports[rid] = r
            else:
                # Optionally aggregate task counts or merge summaries here if needed
                pass

        return list(unique_reports.values())
