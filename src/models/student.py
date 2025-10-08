from datetime import datetime

class Student:
    def __init__(self, student_id: str, name: str, email: str, plan: str, status: str, created_at: datetime = None):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.plan = plan
        self.status = status
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "email": self.email,
            "plan": self.plan,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
