#!/usr/bin/python3
"""
Worker drone surveillance sim
"""

import csv
import requests
from sys import argv

URL_BASE = 'https://jsonplaceholder.typicode.com/users/'


def get_data():
    """This function gets data from the JSONPlaceholder API and exports it to CSV."""
    user_id = argv[1]

    # Fetch user data
    user_data = requests.get(URL_BASE + user_id).json()
    username = user_data['username']

    # Fetch user's todos
    todos = requests.get(URL_BASE + user_id + '/todos/').json()

    # Write data to CSV file
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

            # Write a row to the CSV file
            csv_writer.writerow([
                user_id,
                username,
                task_completed_status,
                task_title
            ])

    # Print a summary
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
