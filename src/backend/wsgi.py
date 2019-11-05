#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module creates the Flask app instance.
Interface to the WSGI server.
"""

import os

from app import create_app

# config_name = "development"
config_name = os.getenv('APP_SETTINGS') 
app = create_app(config_name)

if __name__ == "__main__":
    app.run(threaded=True)
