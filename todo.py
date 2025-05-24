import csv


class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title} | Description: {self.description} | Priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task removed.")
                return
        print("Task not found.")

    def show_tasks(self):
        if not self.tasks:
            print("Task list is empty.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def save_to_file(self, filename="tasks.csv"):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for task in self.tasks:
                    writer.writerow(
                        [task.title, task.description, task.priority])
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_file(self, filename="tasks.csv"):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.tasks = [Task(*row) for row in reader]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")
        except Exception as e:
            print(f"Error loading file: {e}")


def main():
    todo = ToDoList()
    todo.load_from_file()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show All Tasks")
        print("4. Save Tasks to File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            task = Task(title, description, priority)
            todo.add_task(task)
        elif choice == '2':
            title = input("Enter the title of the task to remove: ")
            todo.remove_task(title)
        elif choice == '3':
            todo.show_tasks()
        elif choice == '4':
            todo.save_to_file()
        elif choice == '5':
            todo.save_to_file()
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
