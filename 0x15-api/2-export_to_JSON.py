#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)

    if response.status_code != 200:
        print("User not found")
        sys.exit(1)

    username = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    data = {employee_id: []}
    for task in tasks:
        data[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open(f"{employee_id}.json", 'w') as file:
        json.dump(data, file)
    print(f"Data exported to {employee_id}.json")
