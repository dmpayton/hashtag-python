#!/usr/bin/env python

import argparse
import requests
import sys

twitter_url = 'http://search.twitter.com/search.json?q=from:{username}'

parser = argparse.ArgumentParser(description='Fetch some tweets.')
parser.add_argument('--username', '-u', dest='username',
    help='Twitter username to fetch', required=False)

def main(args):
    ## If a username wasn't passed in, prompt the user
    username = args.username
    if username is None:
        print 'What username would you like to display?'
        username = raw_input('> ')

    message = '\nMost recent tweets from @{0}'.format(username)
    print message
    print '=' * len(message.strip())

    ## Fetch the users feed
    response = requests.get(twitter_url.format(username=username))

    ## No results? I has a sad. :(
    if not response.json['results']:
        print '\nSorry bub, nothing to display for @{0}\n'.format(username)
        return

    ## Print the most recent tweets
    for tweet in response.json['results'][:5]:
        print tweet['created_at']
        print tweet['text']
        print ''

if __name__ == '__main__':
    sys.exit(main(parser.parse_args()))
