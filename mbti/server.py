#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import (Flask, request, render_template)

SERVER = Flask(__name__)
SERVER.config.from_pyfile('settings.py')

if __name__ == '__main__':
    SERVER.run()
