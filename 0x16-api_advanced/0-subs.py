#!/usr/bin/python3
""" Module for task 0 """


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    import requests

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return 0

    return subscribers
