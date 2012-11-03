#!/usr/bin/env python

import json
import sys
import urllib2

twitter_url = 'http://search.twitter.com/search.json?q=from:Hashtag_Fresno'
response = urllib2.urlopen(twitter_url)
data = json.loads(response.read())

for tweet in data['results'][:5]:
    print tweet['created_at']
    print tweet['text']
    print '' # blank line between tweets
