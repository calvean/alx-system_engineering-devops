#!/usr/bin/python3
"""Reddit client"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API and returns a list
     containing the titles of all hot articles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'API Project by Calvean'}
    s = {"limit": 100, "after": after}
    res = requests.get(url, params=s, headers=headers)
    list_a = res.json().get('data', {}).get('children', None)
    page = res.json().get('data', {}).get('after', None)

    if page is not None:
        if list_a:
            for i in list_a:
                hot_list.append(i.get("data").get("title"))
        if page is not None:
            recurse(subreddit, hot_list, page)
        return hot_list
    else:
        return None
