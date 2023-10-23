#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)

    if response.status_code != 200:
        print("User not found")
        sys.exit(1)

    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    total_tasks = len(tasks)

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print("\t{}".format(task.get('title')))
