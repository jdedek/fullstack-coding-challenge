#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module creates the Flask app instance .
Interface to the WSGI server.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(threaded=True)
