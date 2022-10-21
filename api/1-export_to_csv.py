#!/usr/bin/python3
"""
Module
"""
import requests
import sys

if __name__ == '__main__':
user_id = sys.argv[1]
user_url = "https://jsonplaceholder.typicode.com/users/{}"\.format(user_id)
todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\.format(user_id)

user_info = requests.request('GET', user_url).json()
todos_info = requests.request('GET', todo_url).json()

user_name =  user_info["name"]
user_username = user_info["username"]
task_completed = list(filter(lambda obj: (obj["completed"] is True), todos_info))
number_of_tasks = len(task_completed)
total_number_of_tasks = len(todos_info)

width open(str(user_id) + '.csv', "w") as file:
[file.write('"' + str(user_id) + '",' + 
'"' + user_username + '",' +
'"' + str(task["completed"]) + '",' +
'"' + task["title"] + '",' + "\n")
for task in todos_info]
