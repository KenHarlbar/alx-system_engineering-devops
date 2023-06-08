import requests

"""
Function that queries Reddit's API and prints
the titles of the first 10 hot posts listed
for a given subreddit.
"""

def top_ten(subreddit):
    """
    If subreddit is not a valid subreddit, print None
    """
    url = 'https://www.reddit.com/r/{}/hot.json'\
            .format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; \
            Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, \
            params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        for data in response.json().get('data').get('children'):
            print(data.get('data').get('title'))
