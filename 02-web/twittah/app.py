#!/usr/bin/env python

import cherrypy
import os
import requests
from jinja2 import Environment, FileSystemLoader

app_dir = os.path.abspath(os.path.dirname(__file__))
tmpl_dir = os.path.join(app_dir, 'templates')

env = Environment(loader=FileSystemLoader(tmpl_dir))
twitter_url = 'http://search.twitter.com/search.json?q=from:{username}'


class Twittah(object):
    @cherrypy.expose
    def index(self, username=None):
        ## Template context
        context = {'username': username}

        ## Got a username? Get those tweets!
        if username:
            response = requests.get(twitter_url.format(username=username))
            context['tweet_list'] = response.json['results'][:5]

        ## Render the template
        tmpl = env.get_template('twittah.html')
        return tmpl.render(**context)

if __name__ == '__main__':
    cherrypy.quickstart(Twittah())
