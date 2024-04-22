#!/usr/bin/python3
"""gather data from an api"""
import requests
import sys

#!/usr/bin/python3
"""gather data from an api"""

if __name__ == "__main__":
    import requests
    import sys

    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/'
    data = requests.get(url).json()
    data = requests.get(url + 'todos')

    completed = [t for t in data.json() if t.get('completed') is True]

    d = len(completed)
    t = len(data.json())

    print(f"Employee {data.get('name')} is done with tasks({d}/{t}):")
    for i in data.json():
        print(f"\t {i.get('title')}")
