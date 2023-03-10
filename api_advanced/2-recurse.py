#!/usr/bin/python3
"""DOCS"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Prints a list containing the titles
    of all hot articles for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    for child in data['data']['children']:
        hot_list.append(child['data']['title'])
    if data['data']['after'] is None:
        return hot_list
    return recurse(subreddit, hot_list, data['data']['after'])
