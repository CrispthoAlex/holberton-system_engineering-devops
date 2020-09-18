#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None
    Subreddit: A subreddit is a specific online community, and the posts
               associated with it, on the social media website
    """

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    u_Agent = 'Chrome/85.0.4183.102'
    hot_req = requests.get(url, headers={'User-Agent': u_Agent})
    json_hot = hot_req.json()

    if hot_req.status_code != 200:
        return None

    for title in enumerate(json_hot['data']['children']):
        hot_list.append(title[1]['data']['title'])

    if json_hot['data']['after'] is None:
        return []
    return hot_list + recurse(subreddit, hot_list, json_hot['data']['after'])
