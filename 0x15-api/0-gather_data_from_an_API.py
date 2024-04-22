#!/usr/bin/python3
"""gather data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    us_data = requests.get(url + "users/{}".format(argv[1])).json()
    td_data = requests.get(url + "todos", params={"userId": argv[1]}).json()

    comp = [tl.get("title") for tl in td_data if tl.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        us_data.get("name"), len(comp), len(td_data)))
    [print("\t {}".format(c)) for c in comp]
