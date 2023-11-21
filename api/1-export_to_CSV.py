#!/usr/bin/python3
"""
Worker drone surveillance sim
"""

import csv
import requests
from sys import argv

URL_BASE = 'https://jsonplaceholder.typicode.com/users/'


def get_data():
    """
    and export to csv
    """
    user_id = argv[1]

    user_data = requests.get(URL_BASE + user_id).json()
    username = user_data['username']

    todos = requests.get(URL_BASE + user_id + '/todos/').json()

    csv_file_name = '{}.csv'.format(user_id)
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ])

        for item in todos:
            task_completed_status = "True" if item['completed'] else "False"
            task_title = item['title']

            csv_writer.writerow([
                user_id,
                username,
                task_completed_status,
                task_title
            ])

    print(
        'Employee {} is done with tasks({}/{}):\n{}'.format(
            user_data['name'],
            sum(1 for item in todos if item['completed']),
            len(todos),
            csv_file_name
        )
    )


if __name__ == '__main__':
    get_data()
