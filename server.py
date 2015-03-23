#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from mbti import MBTI_BP

SERVER = Flask(__name__)
SERVER.config.from_pyfile('settings.py')

SERVER.register_blueprint(MBTI_BP)

if __name__ == '__main__':
    SERVER.run('0.0.0.0')
