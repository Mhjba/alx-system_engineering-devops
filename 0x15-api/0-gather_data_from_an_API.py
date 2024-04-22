#!/usr/bin/python3
"""gather data from an api"""

if __name__ == "__main__":
    import requests
    import sys

    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/'
    user= requests.get(url).json()
    todos = requests.get(url + 'todos')

    completed = [td for td in todos.json() if td.get('completed') is True]

    dn = len(completed)
    td = len(todos.json())

    print(f"Employee {user.get('name')} is done with tasks({dn}/{td}):")
    for i in todos.json():
        print(f"\t {i.get('title')}")
