#!/usr/bin/python3
"""Contains recurse function"""


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    import requests

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        data = response.json().get(['data'])

        post = data['children'][0]
        hot_list.append(post['data']['title'])
        if len(data['children']) > 1:
            post = data['children'][1]
            hot_list.append(post['data']['title'])
        if data['after']:
            return recurse(subreddit, hot_list=hot_list, after=data['after'])

        return hot_list
