from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks (replace with database for persistence)
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    """Displays the list of tasks."""
    # For reminders, we could sort or filter by due date here
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Adds a new task."""
    global task_id_counter
    task_content = request.form.get('content')
    due_date = request.form.get('due_date') # Basic reminder functionality
    if task_content:
        tasks.append({
            'id': task_id_counter,
            'content': task_content,
            'due_date': due_date,
            'done': False
        })
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggles the done status of a task."""
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes a task."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Use debug=True for development, allows auto-reloading
    app.run(debug=True, port=4000) # Added port=4000
