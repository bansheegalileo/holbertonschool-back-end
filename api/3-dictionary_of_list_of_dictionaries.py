#!/usr/bin/python3
"""
im stressed
"""
import json
import requests
import sys


def record_all_tasks():
    """Gather and print API data"""

    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todo_url = f"{url}/todos"

    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    task_list = [item["title"] for item in todo_data]
    complete_status_list = [item["completed"] for item in todo_data]
    username_list = [user["username"] for user in user_data]

    todo_list = [requests.get(todo_url, params={"userId": i}).json()
                 for i in range(1, len(user_data) + 1)]

    json_dict = {}
    total_counter = 0
    for counter, tasks in enumerate(todo_list, start=1):
        json_list = [
            {
                "username": username_list[counter - 1],
                "task": task_list[total_counter],
                "completed": complete_status_list[total_counter],
            }
            for total_counter in range(total_counter,
                                       total_counter + len(tasks))
        ]
        json_dict[f'{counter}'] = json_list
        total_counter += len(tasks)

    json_object = json.dumps(json_dict)

    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)

if __name__ == "__main__":
    record_all_tasks()
