# Task-CLI: RoadMap.sh's Projects
project URL: [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

### Description:
Task-CLI is a Command line user interface task tracker use to track you task or use as to-do list. This project is one of the practicing project in roadmap.sh. This is also my first time using argparse and learn how to do proper CLI.

## Installation
for installation you can just clone this project.
```bash
$ git clone https://github.com/LylatierN/Task-Cli.git
```

all the library is python builts-in but if you wanna make sure to use the same environment:
```bash
pip install -r requirements.txt
```

## Usage
This project is built for tracking your task and todo list through cmd. With typing command start by `python main.py`

### Features:
- **Add task:** adding task to the database, if the database is not created, create one.
    <br>Using: `python main.py add [task description]`
    ``` bash
    $ python main.py add "cloning task-cli project"
    Task added successfully (ID: 1)
    $ python main.py list                          
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    todo    | 2025-06-20 22:12:46 | 2025-06-20 22:12:46 |
    +----+------------------------------+------------+---------------------+---------------------+
    ```
- **Update task:** Updating your task by id
    <br>Using: `python main.py update [task id] [task description]`
    ``` bash
    $ python main.py update 1 "Watering my plant"  
    Successfully Updated!
    $ python main.py list
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|      Watering my plant       |    todo    | 2025-06-20 22:12:46 | 2025-06-20 22:20:34 |
    +----+------------------------------+------------+---------------------+---------------------+
    ```
- **delete task:** delete task
    <br>Using: `python main.py deleted [task id]`
    ``` bash
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|      Watering my plant       |    todo    | 2025-06-20 22:12:46 | 2025-06-20 22:20:34 |
    |   2|   cloning task-cli project   |    todo    | 2025-06-20 22:24:53 | 2025-06-20 22:24:53 |
    +----+------------------------------+------------+---------------------+---------------------+

    $ python main.py delete 1  
    Successfully remove the task! The task id have been move to fill the removed task

    $ python main.py list    
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    todo    | 2025-06-20 22:24:53 | 2025-06-20 22:24:53 |
    +----+------------------------------+------------+---------------------+---------------------+
- **Mark task:** change the task status into 'in-process' or 'done'
    <br>Using: `python main.py [mark-done / mark-in-process] [task id]`
    ```bash
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    todo    | 2025-06-20 22:24:53 | 2025-06-20 22:24:53 |
    |   2|   cloning task-cli project   |    todo    | 2025-06-20 22:34:28 | 2025-06-20 22:34:28 |
    +----+------------------------------+------------+---------------------+---------------------+

    $ python main.py mark-done 1
    Successfully mark done
    $ python main.py mark-in-process 2
    Successfully mark in-progress

    $ python main.py list
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    done    | 2025-06-20 22:24:53 | 2025-06-20 22:51:08 |
    |   2|   cloning task-cli project   |in-progress | 2025-06-20 22:34:28 | 2025-06-20 22:51:15 |
    +----+------------------------------+------------+---------------------+---------------------+
    ```
- **Show list:** Show the list of task. Can be filtered by status
    <br>Using: `python main.py list` to show all the task
    <br>or : `python main.py lisy [todo/ in-progress]`
    ```bash
    $ python main.py list
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    done    | 2025-06-20 22:24:53 | 2025-06-20 22:51:08 |
    |   2|   cloning task-cli project   |in-progress | 2025-06-20 22:34:28 | 2025-06-20 22:51:15 |
    |   3|       visiting granma        |    todo    | 2025-06-20 22:57:57 | 2025-06-20 22:57:57 |
    |   4|      Cauldron and Coin       |    done    | 2025-06-20 22:58:27 | 2025-06-20 23:20:59 |
    |   5|        Study Calculus        |    todo    | 2025-06-20 23:04:08 | 2025-06-20 23:04:08 |
    +----+------------------------------+------------+---------------------+---------------------+

    $ python main.py list todo
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   3|       visiting granma        |    todo    | 2025-06-20 22:57:57 | 2025-06-20 22:57:57 |
    |   5|        Study Calculus        |    todo    | 2025-06-20 23:04:08 | 2025-06-20 23:04:08 |
    +----+------------------------------+------------+---------------------+---------------------+

    $ python main.py list done
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   1|   cloning task-cli project   |    done    | 2025-06-20 22:24:53 | 2025-06-20 22:51:08 |
    |   4|      Cauldron and Coin       |    done    | 2025-06-20 22:58:27 | 2025-06-20 23:20:59 |
    +----+------------------------------+------------+---------------------+---------------------+

    $ python main.py list in-progress
    +----+------------------------------+------------+---------------------+---------------------+
    | ID |             Task             |   Status   |      CreatedAt      |      CreatedAt      |
    +----+------------------------------+------------+---------------------+---------------------+
    |   2|   cloning task-cli project   |in-progress | 2025-06-20 22:34:28 | 2025-06-20 22:51:15 |
    +----+------------------------------+------------+---------------------+---------------------+
## Sturcture
#### main.py
function:
- **open_file():** open the json file. if there is no file, create one.
- **save_data():** save the data(dict) back into json file
- **check_real(id:int):** check if the id is valid
- **show(data:dict):** show the task in table
- **add(args):** add task into the database
- **update(args):** check the id and update the task
- **delete(args):** delete the task and change the order to fill the removed task's id
- **mark(agrs):** change status
- **show_list(agrs):** filter and show the list
- **main(agrs):** create the parser agrument and command. Execute command.

