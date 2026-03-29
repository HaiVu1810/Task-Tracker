# Task Tracker CLI 

A command-line task management application that allows you to create, update, and track tasks with different statuses.

https://roadmap.sh/projects/task-tracker

## Features

- Add new tasks with descriptions
- Update existing tasks
- Mark tasks as in-progress or done
- Delete individual tasks or all tasks
- List tasks filtered by status
- Persistent storage using JSON

## Project Structure

```
├── task_cli.py           # Main CLI entry point with command handlers
├── task_manager.py       # Core task management logic
├── file_task.json        # Task storage file (auto-created)
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Installation

1. Clone or download the project

## Usage

### Add a Task

Add a new task with a description:

```bash
python task_cli.py Add "Your task description"
```

**Example:**
```bash
python task_cli.py Add "Complete project report"
```

### Update a Task

Update the description of an existing task:

```bash
python task_cli.py Update <task_id> "New task description"
```

**Example:**
```bash
python task_cli.py Update 0 "Updated project report"
```

### Mark Task as In-Progress

Change task status to "in-progress":

```bash
python task_cli.py Mark-In-Progress <task_id>
```

**Example:**
```bash
python task_cli.py Mark-In-Progress 0
```

### Mark Task as Done

Change task status to "done":

```bash
python task_cli.py Mark-Done <task_id>
```

**Example:**
```bash
python task_cli.py Mark-Done 0
```

### Delete a Task

Delete a specific task by ID:

```bash
python task_cli.py Delete <task_id>
```

Delete all tasks:

```bash
python task_cli.py Delete --all
```

**Examples:**
```bash
python task_cli.py Delete 0
python task_cli.py Delete --all
```

### List Tasks

List all tasks:

```bash
python task_cli.py List
```

List tasks by status (todo, in-progress, or done):

```bash
python task_cli.py List <status>
```

**Examples:**
```bash
python task_cli.py List                    # Show all tasks
python task_cli.py List todo               # Show all 'todo' tasks
python task_cli.py List in-progress        # Show 'in-progress' tasks
python task_cli.py List done               # Show completed tasks
```

## Task Data Structure

Tasks are stored in `file_task.json` with the following structure:

```json
{
    "id": 0,
    "description": "Task description",
    "status": "todo",
    "createAt": "Mon Mar 30 02:00:40 2026",
    "updateAt": "Mon Mar 30 03:15:20 2026"
}
```

### Status Values

- **todo**: Task is pending
- **in-progress**: Task is currently being worked on
- **done**: Task is completed

## Technical Details

### Dependencies

- Python 3.x
- argparse (standard library)
- json (standard library)

### Main Components

#### task_cli.py
- Argument parser setup
- Command routing to task operations
- File initialization

#### task_manager.py
- `task_properties` class: Handles all task operations
- `Add_task()`: Creates and stores new tasks
- `Update_task()`: Updates task description or status
- `Del_task()`: Removes tasks
- `List_task()`: Retrieves and displays tasks

## Error Handling

- Handles empty or invalid JSON files gracefully
- Validates task IDs before operations
- Prevents duplicate task descriptions
- Provides user-friendly error messages

## Files

- `file_task.json`: Automatically created on first run, stores all tasks

## Notes

- Task IDs are automatically generated sequentially
- Update timestamps are recorded when tasks are modified
- All times are stored in the user's local timezone format
