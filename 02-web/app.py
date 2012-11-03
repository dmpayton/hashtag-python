#!/usr/bin/env python

import cherrypy
import requests
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))
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


cherrypy.quickstart(Twittah())
