#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    subreddit: A subreddit is a specific online community, and the posts
               associated with it, on the social media website
    """

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    u_Agent = 'Chrome/85.0.4183.102'
    get_req = requests.get(url, headers={'User-Agent': 'python3'})
    json_get = get_req.json()
    if not get_req:
        return 0
    return json_get['data']['subscribers']

if __name__ == '__main__':
    number_of_subscribers(subreddit)
