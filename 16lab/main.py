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
