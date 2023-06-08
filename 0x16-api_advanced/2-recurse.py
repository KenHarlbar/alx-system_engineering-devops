#!/usr/bin/python3
import requests

"""
Make recursive calls to an api
"""


def recurse(subreddit, hot_list=[], after=''):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; \
            Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for data in response.json().get('data').get('children'):
            hot_list.append(data.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
