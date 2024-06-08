Лабораторна робота №16: Advanced TODO List
___
Мета роботи:
In creating programs for checking tasks (to-do list), which provides a convenient interface for adding, viewing and checking tasks. The program can match various attributes such as title, description, expiration date, priority, etc.
___
Опис завдання:
```Python

Task 1: Create Task Class
Create a Python class named Task with the following attributes:
Example of class usage:
Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task
is due today and returns a boolean.
Example of class usage:
Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the
following methods:
title
description
due_date (use datetime.date )
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today() # Expected output: True if today is the due
date
add_task(task: Task)
Example of class usage:
Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returns
a list of tasks that are overdue.
Example of class usage:
Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that
returns a list of tasks that are due today.
Example of class usage:
remove_task(task_title: str)
get_task(task_title: str) -> Task
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries") # Expected output: Task
object
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks() # Expected output: [task1]
from datetime import date
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that
returns a list of tasks sorted by their due dates.
Example of class usage:
Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the
Schedule class that updates the attributes of a task.
Example of class usage:
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today())
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_due_today() # Expected output: [task1,
task2]
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() + timedelta(days=2))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.sort_tasks_by_due_date() # Expected output: [task2,
task1]
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.update_task("Buy groceries", description="Milk, Bread,
Eggs, Cheese", due_date=date(2024, 5, 26))
schedule.get_task("Buy groceries") # Expected output: Task
object with updated attributes
Task 8: Task Status
Add a status attribute to the Task class which can be 'Pending', 'In Progress', or
'Completed'. Modify Task and Schedule to handle task status updates.
Example of class usage:
Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class
that returns a list of tasks for the week starting from the provided date.
Example of class usage:
Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule
class that returns a list of tasks for the specified month.
Example of class usage:
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Pending")
schedule = Schedule()
schedule.add_task(task)
task.status = "In Progress"
schedule.update_task("Buy groceries", status="Completed")
schedule.get_task("Buy groceries").status # Expected output:
"Completed"
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 5, 23))
schedule.add_task(task1)
schedule.add_task(task2)
start_date = date(2024, 5, 20)
schedule.weekly_schedule(start_date) # Expected output: [task1,
task2]
Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'.
Modify Task and Schedule to handle task priority.
Example of class usage:
Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule
class that returns a list of tasks with the specified priority.
Example of class usage:
from datetime import date
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 6, 1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.monthly_schedule(2024, 5) # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
schedule = Schedule()
schedule.add_task(task)
task.priority # Expected output: "High"
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), priority="Low")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_by_priority("High") # Expected output:
[task1]
Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves
the schedule to a file.
Example of class usage:
Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that
loads the schedule from a file.
Example of class usage:
Task 15: Task Notes
Add a notes attribute to the Task class that can store additional information about
the task. Modify Task and Schedule to handle task notes.
Example of class usage:
Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a
list of tasks that have notes.
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.save_to_file("schedule.txt")
schedule = Schedule()
schedule.load_from_file("schedule.txt")
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
schedule = Schedule()
schedule.add_task(task)
task.notes # Expected output: "Use the discount coupon"
Example of class usage:
Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class
that marks the specified task as completed.
Example of class usage:
Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a
list of completed tasks.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_with_notes() # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status # Expected output: "Completed"
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class
that returns a list of tasks that contain the specified keyword in their title or
description.
Example of class usage:
Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of
tasks that are due in the next 24 hours.
Example of class usage:
Task 21: List All Tasks
schedule.add_task(task2)
schedule.list_completed_tasks() # Expected output: [task1]
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment") # Expected output:
[task2]
from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines() # Expected output: [task1]
Add a method list_all_tasks() to the Schedule class that returns a list of all
tasks.
Example of class usage:
Task 22: Task Duration
Add a duration attribute to the Task class which specifies the expected time to
complete the task in hours. Modify Task and Schedule to handle task duration.
Example of class usage:
Task 23: List Tasks by Duration
Add a method list_tasks_by_duration(min_duration: int, max_duration:
int) to the Schedule class that returns a list of tasks whose duration falls within
the specified range.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks() # Expected output: [task1, task2]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration # Expected output: 2
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)
Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of
tasks added, removed, and updated in the schedule.
Example of class usage:
Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes
all completed tasks from the schedule.
Example of class usage:
Task 26: Task Recurrence
Add a recurrence attribute to the Task class that specifies if the task is recurring
(daily, weekly, monthly). Modify Task and Schedule to handle task recurrence.
Example of class usage:
schedule.add_task(task2)
schedule.list_tasks_by_duration(1, 3) # Expected output: [task1]
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history() # Expected output: [("added", task1),
("removed", task1)]
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks() # Expected output: [task2]
Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a
list of recurring tasks.
Example of class usage:
Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the
Schedule class that sets a reminder for a specific task.
Example of class usage:
Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the
percentage of completed tasks.
task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence # Expected output: "weekly"
task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks() # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))
Example of class usage:
Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that
need to be completed before the task can start. Modify Task and Schedule to
handle task dependencies.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage() # Expected output: 50.0
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies # Expected output: [task1]
```
___
Виконання роботи:
```Python
from datetime import date, timedelta
import json

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=0, recurrence=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence

    def is_due_today(self):
        return self.due_date == date.today()

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'status': self.status,
            'priority': self.priority,
            'notes': self.notes,
            'duration': self.duration,
            'recurrence': self.recurrence
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            due_date=date.fromisoformat(data['due_date']),
            status=data.get('status', 'Pending'),
            priority=data.get('priority', 'Medium'),
            notes=data.get('notes', ''),
            duration=data.get('duration', 0),
            recurrence=data.get('recurrence')
        )

    def __repr__(self):
        return f"Task(title={self.title!r}, description={self.description!r}, due_date={self.due_date}, status={self.status!r}, priority={self.priority!r}, notes={self.notes!r}, duration={self.duration}, recurrence={self.recurrence!r})"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(('added', task))

    def remove_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            self.history.append(('removed', task))

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_overdue(self):
        return [task for task in self.tasks if task.due_date < date.today() and task.status != 'Completed']

    def list_due_today(self):
        return [task for task in self.tasks if task.is_due_today() and task.status != 'Completed']

    def sort_by_due_date(self):
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, title, **kwargs):
        task = self.find_task(title)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.history.append(('updated', task))

    def complete_task(self, title):
        task = self.find_task(title)
        if task:
            task.status = "Completed"
            self.history.append(('completed', task))

    def list_completed(self):
        return [task for task in self.tasks if task.status == 'Completed']

    def find_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    def check_deadlines(self):
        tomorrow = date.today() + timedelta(days=1)
        return [task for task in self.tasks if task.due_date == tomorrow]

    def list_all(self):
        return self.tasks

    def list_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def history_log(self):
        return self.history

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if task.status != 'Completed']

    def list_recurring(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, title, reminder_date):
        task = self.find_task(title)
        if task:
            task.reminder_date = reminder_date

    def completion_rate(self):
        total_tasks = len(self.tasks)
        completed_tasks = len(self.list_completed())
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0.0

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [Task.from_dict(data) for data in tasks_data]
            self.history.append(('loaded', filename))

    def execute(self):
        self.add_task(Task("Buy groceries", "Milk, Bread, Eggs", date.today() - timedelta(days=1)))
        self.add_task(Task("Submit assignment", "Math assignment", date.today() + timedelta(days=2)))

        print(self.list_overdue())
        print(self.list_due_today())
        print(self.sort_by_due_date())
        self.update_task("Buy groceries", description="Milk, Bread, Eggs, Cheese", due_date=date(2024, 5, 26))
        self.complete_task("Buy groceries")
        print(self.find_task("Buy groceries").status)
        print(self.list_completed())
        print(self.find_by_keyword("assignment"))
        print(self.check_deadlines())
        print(self.list_all())
        self.add_task(Task("Water plants", "Water the plants in the garden", date(2024, 5, 25), duration=2))
        print(self.list_by_duration(1, 3))
        print(self.history_log())
        self.clear_completed()
        print(self.list_all())
        self.add_task(Task("Water plants", "Water the plants in the garden", date(2024, 5, 25), recurrence="weekly"))
        print(self.list_recurring())
        self.set_reminder("Submit assignment", date(2024, 5, 24))
        print(self.completion_rate())
        self.save_tasks("schedule.txt")
        self.load_tasks("schedule.txt")
        print(self.list_all())

if __name__ == "__main__":
    manager = TaskManager()
    manager.execute()

```
___
Результати:
```Python

[Task(title='Buy groceries', description='Milk, Bread, Eggs', due_date=2024-06-08, status='Pending', priority='Medium', notes='', duration=0, recurrence=None)]
[]
[Task(title='Buy groceries', description='Milk, Bread, Eggs', due_date=2024-06-08, status='Pending', priority='Medium', notes='', duration=0, recurrence=None), Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None)]
Completed
[Task(title='Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=2024-05-26, status='Completed', priority='Medium', notes='', duration=0, recurrence=None)]
[Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None)]
[]
[Task(title='Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=2024-05-26, status='Completed', priority='Medium', notes='', duration=0, recurrence=None), Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None)]
[Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=2, recurrence=None)]
[('added', Task(title='Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=2024-05-26, status='Completed', priority='Medium', notes='', duration=0, recurrence=None)), ('added', Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None)), ('updated', Task(title='Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=2024-05-26, status='Completed', priority='Medium', notes='', duration=0, recurrence=None)), ('completed', Task(title='Buy groceries', description='Milk, Bread, Eggs, Cheese', due_date=2024-05-26, status='Completed', priority='Medium', notes='', duration=0, recurrence=None)), ('added', Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=2, recurrence=None))]
[Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None), Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=2, recurrence=None)]
[Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=0, recurrence='weekly')]
0.0
[Task(title='Submit assignment', description='Math assignment', due_date=2024-06-11, status='Pending', priority='Medium', notes='', duration=0, recurrence=None), Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=2, recurrence=None), Task(title='Water plants', description='Water the plants in the garden', due_date=2024-05-25, status='Pending', priority='Medium', notes='', duration=0, recurrence='weekly')]

```
___
Висновки:
This code creates two classes, Task and TaskManager, to manage a list of tasks. The Task class contains attributes and methods for creating, updating, and representing tasks, as well as for checking whether a task is due today.

The TaskManager class is used to add, delete, and manage tasks. It has methods for performing various operations such as viewing a list of tasks, sorting by due date, updating tasks, and more. It also has functions for saving a task list to a file and loading it from a file.

The execute() function creates sample tasks and then performs various operations using TaskManager methods. At the end, the results of operations are displayed to check the correct operation of the program.
___