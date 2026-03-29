import datetime
import json
class task_properties:
    def __init__(self,description=None,status='todo',createAt=datetime.datetime.now(),id=0):
        self.id=id
        self.description=description
        self.status=status
        self.createAt=createAt.strftime("%c")
        self.task = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createAt": self.createAt,
            "updateAt": ""
        }
    def _load_tasks(self,output_file):
        try:
            with open(output_file) as read_task:
                task_list = json.load(read_task)
                return task_list
        except (json.JSONDecodeError):
            print("File is empty or contains invalid JSON. Initializing with an empty list.")
            return []
        
    def _save_tasks(self,task_list,output_file):
        with open(output_file, 'w') as write_task:
            json.dump(task_list, write_task, indent=4)

    def Add_task(self,output_file):
        task_list = self._load_tasks(output_file)
        if(task_list is not None and len(task_list) >  0):
            self.task["id"]=task_list[-1]["id"] + 1
        for task in task_list:
            if task["description"] == self.description:
                print("Task already exists.")
                return
        task_list.append(self.task)
        self._save_tasks(task_list, output_file)
        print("Task added successfully. with ID:", self.task["id"])

    def Update_task(self,args_id,args_task_name, args_status,output_file):
        task_list = self._load_tasks(output_file)
        if(task_list is None or len(task_list) == 0):
            print("No tasks to update.")
            return
        if(args_id is not None):
            for task in task_list:
                if int(args_id) == task["id"]:
                    old_task=task.copy()
                    if args_task_name is not None:
                        task["description"] = args_task_name
                        print("From:",old_task["description"],"\nTo:",task["description"])

                    if args_status is not None:
                        if task["status"] != args_status:
                            task["status"] = args_status
                            print("Task :",task["description"])
                            print("From:",old_task["status"],"\nTo:",task["status"])
                        else:
                            print(f"Task is already {args_status}.")
                            return
                    task["updateAt"]=datetime.datetime.now().strftime("%c")
                    self._save_tasks(task_list, output_file)

                else:
                    pass
        else:
            print("Must have an ID.")
            for task in task_list:
                print(task)

    def Del_task(self,args_id,args_all,output_file):
        task_list = self._load_tasks(output_file)
        if(task_list is None or len(task_list) == 0):
            print("No tasks to delete.")
            return
        if(args_all):
            task_list.clear()
            self._save_tasks(task_list, output_file)
            print("All tasks deleted successfully.")
            return
        if(args_id is not None):
            for task in task_list:
                if task["id"] == int(args_id):
                    del task_list[task_list.index(task)]
                    self._save_tasks(task_list, output_file)
                    print("Task deleted successfully.")
                    return
                else:
                    pass
        else:
            print("Must have an ID.")
            for task in task_list:
                print(task)

    def List_task(self,output_file,args_Status):
        task_list = self._load_tasks(output_file)
        if(task_list is None or len(task_list) == 0):
            print("No tasks to list.")
            return
        if args_Status is not None:
            for task in task_list:
                if args_Status in task["status"]:
                    print(task)
        else:
            for task in task_list:
                print(task)
