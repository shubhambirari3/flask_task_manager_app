# Flask Task Manager & Reminder

A simple web-based task manager and reminder application built using Flask. This app allows users to add tasks, mark them as done, delete tasks, and optionally set due dates for reminders.

## Features
- Add new tasks with optional due dates.
- Mark tasks as done or undo the "done" status.
- Delete tasks.
- Responsive and user-friendly interface.

## Project Structure
flask_task_manager/ 
├── app.py # Main Flask application 
├── requirements.txt # Python dependencies 
├── templates/ 
│ └── index.html # HTML template for the task manager


## Prerequisites
- Python 3.7 or higher
- Flask 2.0 or higher

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask_task_manager.git
   cd flask_task_manager
   ```

  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  python app.py
  http://127.0.0.1:4000

 ## Future Improvements
Add persistent storage using a database (e.g., SQLite, PostgreSQL).
Implement user authentication for personalized task management.
Add notifications for due tasks.
License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
