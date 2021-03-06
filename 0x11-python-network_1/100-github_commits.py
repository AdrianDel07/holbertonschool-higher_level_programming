#!/usr/bin/python3
"""git commit Module"""
import requests
import sys

if __name__ == '__main__':
    """print all commits 10 times"""
    try:
        repository = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner,
            repository)
        req = requests.get(url)
        R_json = req.json()
        length = len(R_json)
        if length > 10:
            length = 10
        for i in range(length):
            print("{}: {}".format(R_json[i].get('sha'), R_json[i]
                                  .get('commit').get('author').get('name')))
    except Exception:
        print("None")
