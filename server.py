# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template
from mbti import MBTI_BP

SERVER = Flask(__name__)
SERVER.config.from_pyfile('settings.py')


@SERVER.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@SERVER.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


SERVER.register_blueprint(MBTI_BP)

if __name__ == '__main__':
    SERVER.run('0.0.0.0')
