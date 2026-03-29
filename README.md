# Task-Tracker
Task Tracker CLI by Python
usage: task_cli.py [-h] {Add,Update,Mark-In-Progress,Mark-Done,Delete,List} ...

Task Tracker CLI

positional arguments:
  {Add,Update,Mark-In-Progress,Mark-Done,Delete,List}
    Add                 Add a new task
    Update              Update an existing task
    Mark-In-Progress    Mark a task as in-progress
    Mark-Done           Mark a task as done
    Delete              Delete a task
    List                List tasks

options:
  -h, --help            show this help message and exit
Eg:
To Add Task
  usage: task_cli.py Add [-h] Task_description

  positional arguments:
    Task_description  Task description to add

  To Update Task
    usage: task_cli.py Update [-h] id [Task_name]

  positional arguments:
    id          ID of the task to update
    Task_name   New name for the task
  
To Mark Task
  positional arguments:
    id          ID of the task to mark as in-progress/done
  
To Delete Task
  usage: task_cli.py Delete [-h] [--all] [id]

  positional arguments:
    id          ID of the task to delete

  options:
    -h, --help  show this help message and exit
    --all       Delete all tasks
  
To List Task
  usage: task_cli.py List [-h] [{todo,in-progress,done}]

  positional arguments:
    {todo,in-progress,done}

  options:
    -h, --help            show this help message and exit
