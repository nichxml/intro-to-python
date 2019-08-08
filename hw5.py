#!/usr/bin/env python

"""
✓Program loads each "row" of data from ToDo.txt text file into a python Dictionary
20.0 pts
✓Program loads each dictionary "row" into a Python List to create a "Table" of data.
20.0 pts
✓Program displays the table's data to the user.
18.0 pts
✓Program saves the table's data into the ToDo.txt file when the program exits
20.0 pts
✓Upload to GitHub
20.0 pts
✓Feedback
For two points, let us know what you would like feedback on and/or have questions about
2.0 pts
"""

# base data for ToDo.txt (in case my program messes up the original);
# Clean House,low
# Pay Bills,high

infile = "/Users/nichmill/Library/Mobile Documents/com~apple~CloudDocs/C0D3/PycharmProjects/intro_to_python/"

# create empty dictionary to store data as we loop
task_dict = {}

# read in ToDotest.txt here using readlines
with open("ToDo.txt", 'r') as todo_file:
    lines = todo_file.readlines()
for line in lines:
    task = line.split(",")[0].strip()
    priority = line.split(",")[1].strip()
    task_dict[task] = priority

while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line

    # Choice 1 -Show the current items in the table
    if strChoice.strip() == '1':
        print(task_dict)
    # Choice 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        newTask = input("Enter a new task: ")
        newTask = str.title(newTask)
        if newTask in task_dict:
            print("This task already exists.")
        else:
            newPriority = input("Enter a priority for the new task: ")
            newPriority = str.lower(newPriority)
            while not newPriority == "low" and not newPriority == "medium" and not newPriority == "high":
                newPriority = input("Enter a priority for the new task (low, medium or high): ")
            else:
                task_dict[newTask] = newPriority
            task_dict[newTask] = newPriority
    # Choice 3 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        remove_key = input("Enter the task name to remove: ")
        remove_key = str.title(remove_key)
        if remove_key in task_dict:
            del task_dict[remove_key]
            print("Ok, task has been deleted.")
        else:
            print("That task is not in the list.")
    # Choice 4 - Save tasks to the ToDo.txt file
    elif strChoice.strip() == '4':
        with open("ToDo.txt", 'w') as todo_file:
            for key, value in task_dict.items():
                todo_file.write(str(key) + ", " + str(value) + "\n")
        todo_file.close()
    # Choice 5 - end the program
    elif strChoice.strip() == '5':
        with open("ToDo.txt", 'w') as todo_file:
            for key, value in task_dict.items():
                todo_file.write(str(key) + ", " + str(value) + "\n")
        todo_file.close()
        quit()
