#!/usr/bin/python3
""" Python script to fetch and displays an employees  TO DO list """

import requests
import sys


def gettodo_list(employee_id):
    """Fetches and displayes an employees TO DO list
    Args:
    employee_id (int): The employees id
    Return:
        None
    """
    url = f'https://jsonplaceholder.typicode.com/users?id={employee_id}'
    todorl = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response = requests.get(url)
    if response.status_code == 200:
        todo_resp = requests.get(todorl)
        employee_name = response.json()
        todos = todo_resp.json()
        titles = [todo.get("title") for todo in todos if todo.get("completed")]
        header = f"Employee {employee_name[0].get('name')} is done with "\
                f"tasks({len(titles)}/{len(todos)}):"
        print(header)
        for title in titles:
            print(f"\t {title}")

if __name__ == "__main__"
 gettodo_list(sys.argv[1]
