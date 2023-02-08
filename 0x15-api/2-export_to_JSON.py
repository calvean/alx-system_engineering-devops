#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format

Requirementd:/
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
     {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(user_id)).json()
    username = usr.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in todos]}, jsonfile)
