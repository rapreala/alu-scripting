#!/usr/bin/python3
"""
DOC
"""
import requests


def count_words(subreddit, word_list, after='', count={}):
    """
    Recursive function that queries the Reddit API, 
    parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        words = [word.strip('.!,;:?') for word in title.split()]
        for word in words:
            if word in word_list:
                count[word] = count.get(word, 0) + 1

    after = data.get('after')
    if after is None:
        for word in sorted(count.keys(), key=lambda x: (-count[x], x)):
            print('{}: {}'.format(word, count[word]))
        return

    count_words(subreddit, word_list, after, count)
