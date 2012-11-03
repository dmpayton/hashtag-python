#!/usr/bin/env python

import json
import sys
import urllib2

twitter_url = 'http://search.twitter.com/search.json?q=from:{username}'

def main():
    print 'What username would you like to display?'
    username = raw_input('> ')

    message = '\nMost recent tweets from @{0}'.format(username)
    print message
    print '=' * len(message.strip())
    print '' # empty string for a blank line

    ## Fetch the users feed
    response = urllib2.urlopen(twitter_url.format(username=username))
    data = json.loads(response.read())

    ## No results? I has a sad. :(
    if not data['results']:
        print 'Sorry bub, nothing to display for @{0}\n'.format(username)
        return

    ## Print the most recent tweets
    for tweet in data['results'][:5]:
        print tweet['created_at']
        print tweet['text']
        print ''

if __name__ == '__main__':
    sys.exit(main())
