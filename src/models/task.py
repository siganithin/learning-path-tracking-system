import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Add src to path

class Task:
    def __init__(self, task_id, description, status, deadline, plan_id):
        self.task_id = task_id
        self.description = description
        self.status = status  # e.g., "Pending", "Completed"
        self.deadline = deadline
        self.plan_id = plan_id
