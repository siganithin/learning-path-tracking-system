# Learning Path Tracking System

This project is a Learning Path Tracking System application designed to help users manage students, subjects, study plans, tasks, and reports efficiently. It leverages Python, Supabase backend for data storage, and Streamlit for an interactive web interface.

## Features

- **Student Management**: Add, list, and delete students with validation.
- **Subject Management**: Add, list, and delete subjects.
- **Study Plan Creation**: Associate study plans with students and subjects.
- **Task Handling**: Add, update, list, and delete tasks tied to study plans, with status tracking.
- **Reporting**: Generate and view reports summarizing task completion rates for study plans.
- **Progress Visualization**: Streamlit UI includes visual progress indicators showing completion percentage for study plans.
- **Input Validation & Error Handling**: Validations for email, date formats, and robust error handling for database operations ensure data integrity and smooth user experience.

## Technologies Used

- Python 3
- Streamlit for the UI
- Supabase as the backend database and authentication platform
- dotenv for environment variable management

## Project Structure

- `src/cli`: Command-line interface scripts (main.py)
- `src/dao`: Data access objects connecting with Supabase
- `src/models`: Object models for entities like Student, Task, Report, etc.
- `src/services`: Business logic handling for each module
- `app.py`: Streamlit web application interface
- `.env`: Contains Supabase credentials (not included in repo for security)

## Setup Instructions

1. Clone the repository
2. Create a `.env` file and add your Supabase URL and KEY
3. Install the required packages:
4. Run the Streamlit app:

## Usage

- Navigate different sections via sidebar (Students, Subjects, Study Plans, Tasks, Reports).
- Add new entities or manage existing ones.
- Visual progress bars display study plan task completions.
- Generate completion reports based on tasks' status.

## Future Enhancements

- Add user authentication and roles.
- Intuitive UI improvements with search and filters.
- Export reports as PDF or Excel.
- Integration with email reminders for task deadlines.

