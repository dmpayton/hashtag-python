===============
Intro to Python
===============

These are some simple examples for my Intro to Python class, part of the
`Hashtag Academy: Development Mini-Camp <http://hashtagacademy.com/>`_.
These examples fetch the most recent tweets for a given Twitter username.

Class Description
=================

*Saturdays, 3–6 p.m. (Nov. 3, 10, 17)*

Python is a general-purpose programming language, which means that it can be
used for just about everything: websites, desktop applications, games, etc.
This course will cover the basics of programming in Python, including syntax,
built-in datatypes, variables, functions, classes, standard and third-party
libraries, and a bunch more. Whether you’re already a programmer or new to
programming altogether, this class will provide the fundamentals for more
complex coding in Python.

Examples
========

01. Script
----------

The evolution of a simple Python script. Start with the smallest script that
works and build on top of it to make it nicer.

twitter-01.py
~~~~~~~~~~~~~

* The simplest version that could possibly work.

twitter-02.py
~~~~~~~~~~~~~

* Wrap script in a proper ``main()`` function.
* Prompt the user to ender a twitter username.
* Make the output more user-friendly.

twitter-03.py
~~~~~~~~~~~~~

* Add support for passing username through the command line.
* Ditch urllib2 for the (far superior) `requests <http://python-requests.org>`_ library.

02. Web
-------

A very simple web page that displays a form and, on submission, displays a list
of tweets. The following third-party libraries are required:

* `CherryPy <http://cherrypy.org>`_: A very simple web framework
* `Jinja2 <http://jinja.pocoo.org/>`_: A full-featured template engine
* `requests <http://python-requests.org>`_: Dead-simple HTTP requests

To see it in action, simply run ``python app.py`` and open your web browser
to http://localhost:8080/
