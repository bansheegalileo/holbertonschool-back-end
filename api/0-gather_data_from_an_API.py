#!/usr/bin/python3
"""
simulation of worker drone surveilance
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()

    todo_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    todo_data = todo_response.json()

    completed_tasks = [task for task in todo_data if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(todo_data)
    ))

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
