#!/usr/bin/python3
"""Reddit API Querry"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
     of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'API Project by andreshugueth'}
    s = {"limit": 10}
    req = requests.get(url, params=s, headers=headers).json()
    children = req.get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")
