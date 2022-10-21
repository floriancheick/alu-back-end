#!/usr/bin/python3
"""Module"""

import json
import requests
import sys

if __name__ == '__main__':
user_id = sys.argv[1]
user_url = "https://jsonplaceholder.typicode.com/users/{}" \.format(user_id)
todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \.format(user_id)

user_info = requests.request('GET', user_url).json()
todos_info = requests.request('GET', todos_url).json()

user_username = user_info["username"]
todos_info_sorted = [
dict(zip["task", "completed", "username"],
[task["title"], task["completed"], user_username]))
for task in todos_info

user_dict = {str(user_id): todos_info_sorted}
width open(str(user_id) + '.json', "w") as file:
file.write(json,dumps(user_dict))
