import sys
import os
import streamlit as st

# Add src folder for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from services.student_service import StudentService
from services.subject_service import SubjectService
from services.studyplan_service import StudyPlanService
from services.task_service import TaskService
from services.report_service import ReportService

SECTIONS = ["Students", "Subjects", "Study Plans", "Tasks", "Reports"]
st.set_page_config(page_title="Learning Path Tracking System", layout="wide")

with st.sidebar:
    st.markdown("### Dashboard")
    st.markdown("Navigate the sections to manage your learning, tasks, and progress.")
    st.markdown("---")
    section = st.radio("Select Section", SECTIONS, key="section_radio")

st.title(f"Learning Path Tracking System - {section}")

# ----- PAGE LOGIC -----
if section == "Students":
    st.header("Add Student")
    with st.form("add_student_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Add Student")
        if submitted:
            if name and email:
                StudentService.add_student(name, email)
                st.success(f"Student '{name}' added!")
            else:
                st.error("Please enter both name and email.")
    st.header("List of Students")
    students = StudentService.list_students()
    st.table([{ "ID": s["student_id"], "Name": s["name"], "Email": s["email"] } for s in students] if students else [])
    st.header("Delete Student")
    student_options = {f"{s['student_id']} - {s['name']}": s['student_id'] for s in students}
    selected_student = st.selectbox("Select student to delete", list(student_options.keys())) if students else None
    if selected_student:
        if st.button("Delete Student"):
            StudentService.delete_student(student_options[selected_student])
            st.success("Student deleted!")

elif section == "Subjects":
    st.header("Add Subject")
    with st.form("add_subject_form"):
        subject = st.text_input("Subject Name")
        submitted = st.form_submit_button("Add Subject")
        if submitted:
            if subject:
                SubjectService.add_subject(subject)
                st.success(f"Subject '{subject}' added!")
            else:
                st.error("Please enter subject name.")
    st.header("List of Subjects")
    subjects = SubjectService.list_subjects()
    st.table([{ "ID": sub["subject_id"], "Name": sub["name"] } for sub in subjects] if subjects else [])
    st.header("Delete Subject")
    subject_options = {f"{sub['subject_id']} - {sub['name']}": sub['subject_id'] for sub in subjects}
    selected_subject = st.selectbox("Select subject to delete", list(subject_options.keys())) if subjects else None
    if selected_subject:
        if st.button("Delete Subject"):
            SubjectService.delete_subject(subject_options[selected_subject])
            st.success("Subject deleted!")

elif section == "Study Plans":
    st.header("Create Study Plan")
    with st.form("add_plan_form"):
        title = st.text_input("Title")
        students = StudentService.list_students()
        student_options = {f"{s['student_id']}-{s['name']}": s["student_id"] for s in students}
        student_choice = st.selectbox("Select Student", list(student_options.keys())) if students else ""
        subjects = SubjectService.list_subjects()
        subject_options = {f"{sub['subject_id']}-{sub['name']}": sub["subject_id"] for sub in subjects}
        subject_choice = st.selectbox("Select Subject", list(subject_options.keys())) if subjects else ""
        submitted = st.form_submit_button("Create Study Plan")
        if submitted and title and student_choice and subject_choice:
            StudyPlanService.create_studyplan(title, student_options[student_choice], subject_options[subject_choice])
            st.success("Study plan created!")
    st.header("List of Study Plans")
    plans = StudyPlanService.list_studyplans()
    st.table([{ "ID": p["plan_id"], "Title": p["title"], "Student ID": p["student_id"], "Subject ID": p["subject_id"] } for p in plans] if plans else [])
    st.header("Delete Study Plan")
    plan_options = {f"{p['plan_id']} - {p['title']}": p["plan_id"] for p in plans}
    selected_plan = st.selectbox("Select Study Plan to delete", list(plan_options.keys())) if plans else None
    if selected_plan:
        if st.button("Delete Study Plan"):
            StudyPlanService.delete_studyplan(plan_options[selected_plan])
            st.success("Study Plan deleted!")

elif section == "Tasks":
    st.header("Add Task")
    with st.form("add_task_form"):
        plans = StudyPlanService.list_studyplans()
        plan_options = {f"{p['plan_id']}-{p['title']}": p["plan_id"] for p in plans}
        plan_choice = st.selectbox("Select Study Plan", list(plan_options.keys())) if plans else ""
        description = st.text_input("Task Description")
        deadline = st.text_input("Deadline (YYYY-MM-DD)")
        submitted = st.form_submit_button("Add Task")
        if submitted and plan_choice and description and deadline:
            TaskService.add_task(plan_options[plan_choice], description, deadline)
            st.success("Task added!")
    st.header("List of Tasks")
    show_completed = st.checkbox("Show completed tasks")
    tasks = TaskService.list_tasks()
    if not show_completed:
        tasks = [t for t in tasks if t["status"] != "Completed"]
    st.table([{ "ID": t["task_id"], "Description": t["description"], "Status": t["status"], "Deadline": t["deadline"], "Plan ID": t["plan_id"] } for t in tasks] if tasks else [])
    st.header("Update Task Status")
    task_options = {f"{t['task_id']} - {t['description']} [{t['status']}]": t['task_id'] for t in tasks}
    selected_task = st.selectbox("Select Task to Update", list(task_options.keys())) if tasks else None
    if selected_task:
        new_status = st.selectbox("New Status", ["Pending", "Completed"])
        if st.button("Update Status"):
            TaskService.update_task(task_options[selected_task], status=new_status)
            st.success("Task status updated!")
    st.header("Delete Task")
    selected_task_del = st.selectbox("Select Task to Delete", list(task_options.keys())) if tasks else None
    if selected_task_del:
        if st.button("Delete Task"):
            TaskService.delete_task(task_options[selected_task_del])
            st.success("Task deleted!")

elif section == "Reports":
    st.header("Generate Report")
    with st.form("generate_report_form"):
        plans = StudyPlanService.list_studyplans()
        plan_options = {f"{p['plan_id']}-{p['title']}": p["plan_id"] for p in plans}
        plan_choice = st.selectbox("Select Study Plan", list(plan_options.keys())) if plans else ""
        submitted = st.form_submit_button("Generate Report")
        if submitted and plan_choice:
            ReportService.generate_report(plan_options[plan_choice])
            st.success("Report generated!")
    st.header("View Reports")
    plan_filter = st.text_input("Filter by Study Plan ID (leave blank for all):")
    reports = ReportService.view_report(int(plan_filter) if plan_filter else None)
    unique_reports = {}
    for r in reports:
        pid = r["plan_id"]
        if pid not in unique_reports:
            unique_reports[pid] = r
    st.table([{ "Report ID": rep["report_id"], "Plan ID": rep["plan_id"], "Summary": rep["summary"] }
        for rep in unique_reports.values() ])
