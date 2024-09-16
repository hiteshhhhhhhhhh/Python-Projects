Description:
This Python script is a command-line to-do list application called "TaskMaster". It allows users to interact with a list of tasks through a menu-driven interface. Here's a brief description of how it works:

The program starts by importing the tabulate library, which is used for formatting and displaying tables in the console.

The main function is the entry point of the program. It initializes a list called database to store tasks and a variable count to keep track of the number of tasks.

Inside the main function, there is a loop (while running:) that continues until the user chooses to exit.

The get_input function displays a menu of options (View Tasks, Create a Task, Update a Task, Delete a Task, and Exit) and prompts the user for their choice. It validates the input to ensure it corresponds to a valid option.

Depending on the user's choice, one of the following actions is performed:

"V": View tasks. Calls the view function to display the current list of tasks.
"C": Create a task. Calls the create function to add a new task to the list.
"U": Update a task. Calls the update function to modify an existing task.
"D": Delete a task. Calls the delete function to remove a task from the list.
"E": Exit the program. Sets running to False, which will terminate the loop and end the program.
The view function uses the tabulate library to display the tasks in a formatted table.

The create function prompts the user for a new task, assigns it a unique ID, and adds it to the database.

The update function allows the user to select a task by its ID, then provides an option to change the task's description.

The delete function allows the user to select a task by its ID and removes it from the database.

If the user chooses to exit the program, the main function ends, and the program terminates.

Overall, this script provides a simple and functional command-line interface for managing a to-do list.


A command-line interface to-do list created using Python

youtube link:
https://youtu.be/b5b_Fj5j_RU

Installation and use:
Use pip to install the package tabulate
$ pip install tabulate

Use python to run the application

$ python project.py
Use pytest to test the application

$ pytest test_project.py

contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
