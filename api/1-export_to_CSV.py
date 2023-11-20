#!/usr/bin/python3
"""
export to csv
"""

import csv
from requests import get
from sys import argv

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_csv():
    user_data = get(url_base + argv[1]).json()
    tasks_data = get(url_base + argv[1] + '/todos').json()
    file_name = argv[1] + '.csv'

    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        for task in tasks_data:
            csv_writer.writerow([user_data['id'], user_data['username'],
                                 task['completed'], task['title']])


if __name__ == '__main__':
    export_csv()
