#!/usr/bin/python3
"""
For a given employee, returns information about the TODO list progress
Displays:/
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    id_ = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)

    req = requests.Session()

    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)
    response = req.get(url2)
    name = response.json()['username']

    response = req.get(url)
    body = response.json()

    with open(id_ + '.csv', mode='w') as csv_file:
        employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)

        for i in body:
            employee_writer.writerow([id_, name, i['completed'],
                                      i['title']])
