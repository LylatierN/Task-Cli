import argparse
import json
import os
from datetime import datetime

FILENAME: str = 'data.json'

task_list: dict = {}
args = None

# "1":{'id': 1, 'task':'name, status: "to-do"}

def open_file():
    # check if there is any file created
    if os.path.isfile(FILENAME):
        with open(FILENAME) as json_file:
            prog_dict = json.load(json_file)
    else:
        prog_dict = {}
        save_data(prog_dict)
    return prog_dict

def save_data(_data=task_list):
    with open(FILENAME, mode="w", encoding="utf-8") as write_file:
        json.dump(_data, write_file, indent=4)

def check_real(id: int):
    return str(id) in task_list

def show(data: dict):
    print(f'+{"-"*4}+{"-"*30}+{"-"*10}+{"-"*21}+{"-"*21}+')
    print(f'|{"ID":^4}|{"Task":^30}|{"Status":^10}|{"CreatedAt":^21}|{"CreatedAt":^21}|')
    print(f'+{"-"*4}+{"-"*30}+{"-"*10}+{"-"*21}+{"-"*21}+')
    for task in data.values():
        print(f'|{task["id"]:>4}|{task["task"]:^30}|{task["status"]:^10}|{task["createdAt"]:^21}|{task["updatedAt"]:^21}|')
    print(f'+{"-"*4}+{"-"*30}+{"-"*10}+{"-"*21}+{"-"*21}+')


def add(args):
    # add data here
    global task_list
    id = (len(task_list)+1)

    #add task
    task_list[str(len(task_list)+1)] = {'id': id, 
                                        'task':args.task, 
                                        'status':'todo', 
                                        'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    print(f"Task added successfully (ID: {id})")


def update(args):
    global task_list
    #check if task is real
    if check_real(args.id):
        #update
        id = args.id
        task_list[str(id)]['task'] = args.task
        task_list[str(id)]['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Successfully Updated!")
    else:
        print("Sorry, there is no task in that id")

def delete(args): 
    global task_list
    #check if task is real
    if not check_real(args.id):
        print("Sorry, there is no task in that id")
        return False
    
    # delete
    removed = args.id
    amount = len(task_list)
    for i in range(removed, amount):
        task_list[str(i)] = task_list[str(i + 1)]
        
    del task_list[str(amount)]

    # notice the user
    txt = "Successfully remove the task!"
    if removed != amount:
        txt += " The task id have been move to fill the removed task"
    print(txt)

def mark(agrs):
    global task_list
    #check if task is real
    if not check_real(args.id):
        print("Sorry, there is no task in that id")
        return False
    id = args.id
    status = 'todo'
    if args.command == 'mark-done':
        status = 'done'
    if args.command == 'mark-in-process':
        status = 'in-progress'
    task_list[str(id)]['status'] = status
    task_list[str(id)]['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # notice the user
    print(f'Successfully mark {status}') 

def show_list(agrs):
    global task_list
    
    # choose list
    if args.type == 'all':
        show(task_list)
        return True
    
    type = args.type
    # create a copy
    tmp = task_list.copy()
    for key, values in tmp.items():
        if values['status'] != type:
            tmp.pop(key)
    show(tmp)

####################################

def main():
    global task_list, args
    task_list = open_file()

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    # add
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("task")
    add_parser.set_defaults(func=add)

    # update
    update_parser = subparser.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("task")
    update_parser.set_defaults(func=update)

    # delete
    delete_parser = subparser.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    delete_parser.set_defaults(func=delete)

    # mark in process
    markprocess_parser = subparser.add_parser("mark-in-process")
    markprocess_parser.add_argument("id", type=int)
    markprocess_parser.set_defaults(func=mark)

    # mark done
    markdone_parser = subparser.add_parser("mark-done")
    markdone_parser.add_argument("id", type=int)
    markdone_parser.set_defaults(func=mark)

    # show list
    list_parser = subparser.add_parser("list")
    list_parser.add_argument("type", choices=['all', 'todo', 'done', 'in-progress'], default='all', nargs='?')
    list_parser.set_defaults(func=show_list)

    args = parser.parse_args()
    # print(args)
    args.func(args)
    save_data(task_list)

if __name__ == "__main__":
    main()