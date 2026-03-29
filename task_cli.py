import argparse
from task_manager import task_properties
import os
def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')
    # Add positional and optional arguments
    add_parser = subparsers.add_parser('Add', help='Add a new task')
    add_parser.add_argument('Task_description', help='Task description to add')

    update_parser = subparsers.add_parser('Update', help='Update an existing task')
    update_parser.add_argument('id', help='ID of the task to update')
    update_parser.add_argument('Task_name', help='New name for the task', nargs='?', default=None)
    
    mark_in_progress_parser = subparsers.add_parser('Mark-In-Progress', help='Mark a task as in-progress')
    mark_in_progress_parser.add_argument('id', help='ID of the task to mark as in-progress')

    mark_done_parser = subparsers.add_parser('Mark-Done', help='Mark a task as done')
    mark_done_parser.add_argument('id', help='ID of the task to mark as done')

    delete_parser = subparsers.add_parser('Delete', help='Delete a task')
    delete_parser.add_argument('id', nargs='?', help='ID of the task to delete')
    delete_parser.add_argument('--all', action='store_true', help='Delete all tasks')

    list_parser = subparsers.add_parser('List', help='List tasks')
    list_parser.add_argument('status', nargs='?', default=None, 
                                choices=['todo', 'in-progress', 'done'])

    # Parse argument
    args = parser.parse_args()
    # out_put_file=args.output_file + ".json"
    filename="file_task.json"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            print("File created successfully.")

    # Initialize with an empty list if the file doesn't exist
    if args.command == 'Add':
        task_handler=task_properties(args.Task_description)
        task_handler.Add_task(filename)
    elif args.command == 'Update':
        task_handler=task_properties(args.Task_name)
        task_handler.Update_task(args.id,args.Task_name,None, filename)
    elif args.command == 'Mark-In-Progress':
        task_handler=task_properties()
        task_handler.Update_task(args.id, None, 'in-progress', filename)
    elif args.command == 'Mark-Done':
        task_handler=task_properties()
        task_handler.Update_task(args.id, None, 'done', filename)
    elif args.command == 'Delete':
        task_handler=task_properties()
        if args.all:
            task_handler.Del_task(None,args.all,filename)
        else:
            task_handler.Del_task(args.id,False,filename)
    elif args.command == 'List':
        task_handler=task_properties()
        task_handler.List_task(filename,args.status)
if __name__ == "__main__":
    main()