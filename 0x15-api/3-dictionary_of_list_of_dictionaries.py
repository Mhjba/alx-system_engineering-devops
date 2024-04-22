#!/usr/bin/python3
"""Export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests

    users_path = '/users'
    url = "https://jsonplaceholder.typicode.com/"
    us_data = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": us.get("username")
            }
              for task in requests.get(url + "todos",
                                       params={"userId": us.get("id")}).json()]
            for us in us_data}, jsonfile)
