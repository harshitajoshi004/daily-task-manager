import sqlite3
tasks = []
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")

connection.commit()
while True:
  print("===== DAILY TASK MANAGER =====")

  print("1. Add Task")
  print("2. View Tasks")
  print("3. Complete Task")
  print("4. Delete Task")
  print("5. Search Task")
  print("6. Exit")
  choice = input("Enter your choice: ")

  if choice == "1":
    task = input("Enter your task: ")

    cursor.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (task,)
    )

    connection.commit()

    print("Task added successfully!")

  elif choice == "2":
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()

    if len(all_tasks) == 0:
        print("No tasks available.")

    else:
        print("\nYour Tasks:")

        for task in all_tasks:
            print(task[0], ".", task[1])

  elif choice == "3":
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()

    if len(all_tasks) == 0:
        print("No tasks available.")

    else:
        print("\nYour Tasks:")

        for task in all_tasks:
            status = "Completed" if task[2] == 1 else "Pending"
            print(task[0], ".", task[1], "-", status)

        task_number = int(input("Enter task number to complete: "))

        cursor.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_number,)
        )

        connection.commit()

        print("Task completed successfully!")
  elif choice == "4":
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()

    if len(all_tasks) == 0:
        print("No tasks available.")

    else:
        print("\nYour Tasks:")

        for task in all_tasks:
            print(task[0], ".", task[1])

        task_number = int(input("Enter task number to delete: "))

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_number,)
        )

        connection.commit()

        print("Task deleted successfully!")
  elif choice == "5":
    search = input("Enter task to search: ")

    cursor.execute(
        "SELECT * FROM tasks WHERE LOWER(task) LIKE LOWER(?)",
        ("%" + search + "%",)
    )

    results = cursor.fetchall()

    if len(results) == 0:
        print("Task not found.")

    else:
        print("\nSearch Results:")

        for task in results:
            status = "Completed" if task[2] == 1 else "Pending"
            print(task[0], ".", task[1], "-", status)

  elif choice == "6":
    print("Goodbye!")

  else:
    print("Invalid choice. Please try again.")