#!/usr/bin/python3
"""
Python script that for a given employee ID, returns information
about his/her TODO list progress.
Adding features:
    * Export data in the CSV format.
    * Export data in the JSON format.
"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/'
    req_user = requests.get("{}users".format(url)).json()
    req_todo = requests.get("{}todos".format(url)).json()

    # Export to JSON
    with open('todo_all_employees.json', 'w') as task_file:

        data = {}
        for user in req_user:
            list_task = []
            for task in req_todo:
                if task['userId'] == user['id']:
                    list_task.append({
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": user['username']
                    })
            data[user['id']] = list_task
        json.dump(data, task_file)
