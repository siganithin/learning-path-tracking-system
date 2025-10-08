<<<<<<< HEAD
import sys
import os

# Add src folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from services.student_service import StudentService
from services.subject_service import SubjectService
from services.studyplan_service import StudyPlanService
from services.task_service import TaskService
from services.report_service import ReportService


def main_menu():
    while True:
        print("\n--- Study Planner ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Subject")
        print("4. List Subjects")
        print("5. Create Study Plan")
        print("6. List Study Plans")
        print("7. Add Task")
        print("8. List Tasks")
        print("9. Generate Report")
        print("10. View Reports")
        print("11. Exit")  # Exit at last
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            StudentService.add_student(name, email)

        elif choice == "2":
            StudentService.list_students()

        elif choice == "3":
            name = input("Enter subject name: ")
            SubjectService.add_subject(name)

        elif choice == "4":
            SubjectService.list_subjects()

        elif choice == "5":
            title = input("Enter study plan title: ")
            student_id = input("Enter student ID: ")
            subject_id = input("Enter subject ID: ")
            StudyPlanService.create_studyplan(title, student_id, subject_id)

        elif choice == "6":
            student_filter = input("Enter student ID to filter (or leave blank for all): ")
            student_filter = int(student_filter) if student_filter else None
            StudyPlanService.list_studyplans(student_filter)

        elif choice == "7":
            plan_id = input("Enter Study Plan ID: ")
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            TaskService.add_task(plan_id, description, deadline)

        elif choice == "8":
            plan_filter = input("Enter Study Plan ID to filter (or leave blank for all): ")
            plan_filter = int(plan_filter) if plan_filter else None
            TaskService.list_tasks(plan_filter)

        elif choice == "9":
            plan_id = input("Enter Study Plan ID: ")
            ReportService.generate_report(plan_id)

        elif choice == "10":
            plan_filter = input("Enter Study Plan ID to filter (or leave blank for all): ")
            plan_filter = int(plan_filter) if plan_filter else None
            ReportService.view_report(plan_filter)

        elif choice == "11":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
=======
import sys
import os

# Add src folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from services.student_service import StudentService
from services.subject_service import SubjectService
from services.studyplan_service import StudyPlanService
from services.task_service import TaskService
from services.report_service import ReportService

def main_menu():
    while True:
        print("\n--- Study Planner ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Subject")
        print("4. List Subjects")
        print("5. Create Study Plan")
        print("6. List Study Plans")
        print("7. Add Task")
        print("8. List Tasks")
        print("9. Generate Report")
        print("10. View Reports")
        print("11. Exit")  # Exit at last
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            StudentService.add_student(name, email)

        elif choice == "2":
            StudentService.list_students()

        elif choice == "3":
            name = input("Enter subject name: ")
            SubjectService.add_subject(name)

        elif choice == "4":
            SubjectService.list_subjects()

        elif choice == "5":
            title = input("Enter study plan title: ")
            student_id = input("Enter student ID: ")
            subject_id = input("Enter subject ID: ")
            StudyPlanService.create_studyplan(title, student_id, subject_id)

        elif choice == "6":
            student_filter = input("Enter student ID to filter (or leave blank for all): ")
            student_filter = int(student_filter) if student_filter else None
            StudyPlanService.list_studyplans(student_filter)

        elif choice == "7":
            plan_id = input("Enter Study Plan ID: ")
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            TaskService.add_task(plan_id, description, deadline)

        elif choice == "8":
            plan_filter = input("Enter Study Plan ID to filter (or leave blank for all): ")
            plan_filter = int(plan_filter) if plan_filter else None
            TaskService.list_tasks(plan_filter)

        elif choice == "9":
            plan_id = input("Enter Study Plan ID: ")
            ReportService.generate_report(plan_id)

        elif choice == "10":
            plan_filter = input("Enter Study Plan ID to filter (or leave blank for all): ")
            plan_filter = int(plan_filter) if plan_filter else None
            ReportService.view_report(plan_filter)

        elif choice == "11":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
>>>>>>> 43fa1d364497bf14423a758edbaafb358bec959f
