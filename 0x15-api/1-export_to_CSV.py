#!/usr/bin/python3
"""gather data from an api"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    us_data = requests.get(url + "users/{}".format(user_id)).json()
    user_name = us_data.get("username")
    td_data = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, td.get("completed"), td.get("title")]
         ) for td in td_data]
