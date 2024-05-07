#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """ Queries the Reddit API """
    import requests

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        hot_posts = data.get('children')

        for post in hot_posts:
            print(post['data']['title'])

    print(None)
