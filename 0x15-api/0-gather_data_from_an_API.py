#!/usr/bin/python3
"""
For a given employee, returns information about the TODO list progress

Display:/
    First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks,
        which is the sum of completed and non-completed tasks

    Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE
"""
import requests
from sys import argv


if __name__ == '__main__':
    id_ = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)

    req = requests.Session()

    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)
    response = req.get(url2)
    name = response.json()['name']

    response = req.get(url)
    body = response.json()
    tasks_done = []

    for i in body:
        if i['completed']:
            tasks_done.append('\t ' + i['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(tasks_done), len(body)))
    print(*tasks_done, sep='\n')
