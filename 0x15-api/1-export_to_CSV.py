#!/usr/bin/python3
"""
Python script that for a given employee ID, returns information
about his/her TODO list progress.
Adding features:
    * Export data in the CSV format.
"""
import csv
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
    name_csv = "{}.csv".format(user_id)

    with open(name_csv, mode='w') as user_task:
        writer = csv.writer(user_task, delimiter=',', quoting=csv.QUOTE_ALL)

        for dic_do in req_todo:
            writer.writerow([user_id, user_name, dic_do['completed'],
                             dic_do['title']])
