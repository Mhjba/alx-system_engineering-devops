#!/usr/bin/python3
"""gather data from an api"""
from requests import get
from sys import argv

if __name__ == "__main__":
        url = get("https://jsonplaceholder.typicode.com/")
            user = requests.get(url + "users/{}".format(argv[1])).json()
                todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

                    completed = [i.get("title") for i in todos if i.get("completed") is True]
                        print("Employee {} is done with tasks({}/{}):".format(
                                    user.get("name"), len(completed), len(todos)))
                            [print("\t {}".format(c)) for c in completed]
