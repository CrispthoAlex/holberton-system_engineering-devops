#!/usr/bin/python3
"""
Python script that for a given employee ID, returns information
about his/her TODO list progress
"""
import requests
from sys import argv


url = 'https://jsonplaceholder.typicode.com/'
user_id = argv[1]
req_user = "{}users/{}".format(url, user_id)
user_name = requests.get(req_user).json().get('name')
todo_true = "{}todos?userId={}".format(url, user_id)
req_todo = requests.get(todo_true).json()
# Get numbers of elements
elements = list(dic_do['completed'] for dic_do in req_todo)
total_ele = len(elements)  # Elements total
task_do = elements.count(True)  # Task done for the employee

# Print line
print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                      task_do, total_ele))

# print title
for dic_do in req_todo:
    if dic_do['completed'] is True:
        print('\t ' + dic_do['title'])
