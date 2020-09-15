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
    user_id = argv[1]
    req_user = "{}users/{}".format(url, user_id)
    name = requests.get(req_user).json().get('name')
    user_name = requests.get(req_user).json().get('username')
    todo_user = "{}todos?userId={}".format(url, user_id)
    req_todo = requests.get(todo_user).json()

    # Get numbers of elements
    elements = list(dic_do['completed'] for dic_do in req_todo)
    total_ele = len(elements)  # Elements total
    task_do = elements.count(True)  # Task done for the employee

    # Export to CSV
    name_json = "{}.json".format(user_id)

    with open(name_json, 'w') as task_file:
        list_task = []
        for dic_do in req_todo:
            list_task.append({
                "task": dic_do['title'],
                "completed": dic_do['completed'],
                "username": user_name
            })
        data = {user_id: list_task}
        json.dump(data, task_file)
