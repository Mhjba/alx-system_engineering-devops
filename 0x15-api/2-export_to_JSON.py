#!/usr/bin/python3
"""gather data from an api"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    us_data = requests.get(url + "users/{}".format(user_id)).json()
    user_name = us_data.get("username")
    td_data = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_name
            } for t in td_data]}, jsonfile)
