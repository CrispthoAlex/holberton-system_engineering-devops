#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    Subreddit: A subreddit is a specific online community, and the posts
               associated with it, on the social media website
    """

    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    u_Agent = 'Chrome/85.0.4183.102'
    top10_req = requests.get(url, headers={'User-Agent': u_Agent})
    json_top10 = top10_req.json()
    if not top10_req.status_code == 200:
        return None
    for title in enumerate(json_top10['data']['children']):
            print(title[1]['data']['title'])


if __name__ == '__main__':
    """from sys import argv
    subreddit = argv[1]"""
    top_ten(subreddit)
