import validation
import uuid
import sys
import os
import utility


def MainMenu():
  """
  Presents the main menu to the user and gets their choice.

  Returns:
      int: The user's choice (1-4).
  """
  print(" TODO LIST ".center(21, '='))
  print("1. Show Current Tasks")
  print("2. Add A Task")
  print("3. Complete A Task")
  print("4. Exit")
  choice=validation.GetIntValue("What would you like to do? ", 1, 4)
  return choice

def RunProgram():
  """
  Runs the main program loop for the to-do list application.
  Initializes the ToDoList, presents the main menu, and processes user input
  until the user chooses to exit.  Saves tasks to a file upon exiting.
  """
  todoList=ToDoList()
  userChoice=0
  while userChoice != 4:
    userChoice=MainMenu()
    if userChoice==1:
      todoList.show_tasks()
    elif userChoice==2:
      todoList.add_task()
    elif userChoice==3:
      todoList.complete_task()
  else:
    print("Thank you for using the program!")
    todoList.save_tasks_to_file()

class ToDoList:

  def __init__(self):
    self.__todo_list = []
    self.__read_from_file()

  def __get_task_count(self):
    """Returns the number of items in the todo list"""
    return len(self.__todo_list)

  def __read_from_file(self):
    """
    Reads tasks from the 'todoList.txt' file and populates the todo list.
    If the file doesn't exist, it creates a new one. Handles potential
    IOErrors during file operations.
    """
    stream = None
    try:
      stream = open("todoList.txt", 'rt')
      lines = stream.readlines()
      for line in lines:
        task = tuple(line.strip().split(';'))
        self.__todo_list.append(task)
    except FileNotFoundError:
      print("No todolist file detected. Creating new one")
      newList = open('todoList.txt', 'w')
      newList.close()
    except IOError as exception:
      print("I/O error occurred: ", os.strerror(exception.errno))
      sys.exit()
    finally:
      if stream:
        stream.close()

  def save_tasks_to_file(self):
    """
    Saves the current list of tasks to the 'todoList.txt' file.
    Each task is written as a line in the file, with task details
    separated by semicolons. Handles potential IOErrors during file operations.
    """
    try:
      stream = open("todoList.txt", 'wt')
      for task in self.__todo_list:
        output = ';'.join(task)
        stream.write(output + "\n")
      stream.close()
    except IOError as exception:
      print("I/O error occurred: ", os.strerror(exception.errno))

  def __check_task_exists(self, task_name):
    """Checks if the task entered by user already exists in the list

    Returns: true if exists, false if not
    """
    if self.__get_task_count() == 0:
      return False

    for task in self.__todo_list:
      if task_name == task[1]:
        return True
    return False

  def show_tasks(self):
    """
    Displays the current tasks in the to-do list.

    The tasks are retrieved from the internal todo list and printed
    to the console, along with their deadline. If the list is empty,
    a message indicating that there are no current tasks is displayed.
    """

    utility.clear_console()
    print("Current Tasks".center(20, '*'))
    print('-' * 20)
    if self.__get_task_count() == 0:
      print("No current tasks")
    else:
      for i in range(len(self.__todo_list)):
        print(f"{i+1}. {self.__todo_list[i][1]} | {self.__todo_list[i][2]}")
    print('-' * 20)
    print()

  def add_task(self):

    """
    Adds a new task to the to-do list.

    Prompts the user for the task description and deadline.
    Generates a unique ID for the task and stores the task
    details in the todo list. Prevents duplicate task names.
    """
    while True:
      task = input("What is the task? ")
      if self.__check_task_exists(task):
        print(
            "It looks like you already have a task with that name.\nPlease enter a new one."
        )
        continue
      break
    deadline = input("When is it due? ")
    id = str(uuid.uuid4())
    taskTuple = (id, task, deadline)
    self.__todo_list.append(taskTuple)

  def complete_task(self):

    """
    Marks a task as complete by removing it from the to-do list.

    Displays the current list of tasks to the user and prompts them
    to select the task they want to complete. Removes the selected
    task from the list and redisplays the updated list.
    If the list is empty, informs the user that there are no tasks
    to complete.
    """
    if self.__get_task_count()==0:
      print("\nThere are currently no tasks to complete.\n")
      return

    self.show_tasks()
    task = validation.GetIntValue("Which task do you want to complete? ", 1,
                                  len(self.__todo_list))
    self.__todo_list.pop(task - 1)
    self.show_tasks()

if __name__ == '__main__':
  RunProgram()
