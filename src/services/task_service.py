<<<<<<< HEAD
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

from dao.db_config import supabase

class TaskService:
    @staticmethod
    def add_task(plan_id, description, deadline):
        data = {
            "plan_id": plan_id,
            "description": description,
            "status": "Pending",
            "deadline": deadline
        }
        supabase.table("task").insert(data).execute()
        print("Task added successfully!")

    @staticmethod
    def update_task(task_id, description=None, status=None):
        data = {}
        if description:
            data["description"] = description
        if status:
            data["status"] = status
        if data:
            supabase.table("task").update(data).eq("task_id", task_id).execute()
            print("Task updated successfully!")
        else:
            print("Nothing to update.")

    @staticmethod
    def list_tasks(plan_id=None):
        query = supabase.table("task").select("*")
        if plan_id:
            query = query.eq("plan_id", plan_id)
        tasks = query.execute()
        return tasks.data if tasks.data else []
    @staticmethod
    def delete_task(task_id):
        supabase.table("task").delete().eq("task_id", task_id).execute()
        print(f"Task {task_id} deleted.")


=======
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

from dao.db_config import supabase

class TaskService:
    @staticmethod
    def add_task(plan_id, description, deadline):
        data = {
            "plan_id": plan_id,
            "description": description,
            "status": "Pending",
            "deadline": deadline
        }
        supabase.table("task").insert(data).execute()
        print("Task added successfully!")

    @staticmethod
    def update_task(task_id, description=None, status=None):
        data = {}
        if description:
            data["description"] = description
        if status:
            data["status"] = status
        if data:
            supabase.table("task").update(data).eq("task_id", task_id).execute()
            print("Task updated successfully!")
        else:
            print("Nothing to update.")

    @staticmethod
    def list_tasks(plan_id=None):
        query = supabase.table("task").select("*")
        if plan_id:
            query = query.eq("plan_id", plan_id)
        tasks = query.execute()
        if tasks.data:
            for t in tasks.data:
                print(f"{t['task_id']} - {t['description']} [{t['status']}] (Plan ID: {t['plan_id']})")
        else:
            print("No tasks found.")
>>>>>>> 43fa1d364497bf14423a758edbaafb358bec959f
