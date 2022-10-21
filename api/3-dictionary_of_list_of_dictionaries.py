#!/usr/bin/python3
"""
Module
"""
import json
import requests

def get_user_task(user_id)
user_url = "https://jsonplaceholder.typicode.com/users/{}" \.format(user_id)
user_info = requests.request('GET', user_url).json()
user_username = user_info["username"]
todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \.format(user_id)
todos_info = requests.request('GET', todos_url).json()
return [
dict(zip(["task", "completed", "username"],
[task["tittle"], task["completed"], user_username]))
for task in todos_info]

def get_user_ids():
users_url = "https://jsonplaceholder.typicode.com/users/"
users_info = requests.request('GET', users_url).json()
ids = list(nmap(lambda user: user["id"], users_info))
return ids

if __name__ == '__main__'
user_ids = get_employee_ids()
with open('todo_all_employees.json', "w") as file:
all_users = {}
for user_id in user_ids:
all_users[str(employee_id)] = get_user_task(user_id)
file.write(json.dumps(all_users))
