#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    return user, todos, completed_tasks

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as argument.")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_info, tasks_info, completed_tasks = get_todo_list(employee_id)

    print("Employee {} has completed {}/{} tasks:".format(
        user_info.get("name"), len(completed_tasks), len(tasks_info)))
    for task in completed_tasks:
        print("\t", task)
