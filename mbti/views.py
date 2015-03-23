#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from flask import render_template
from flask import Blueprint
from flask import abort
from flask import request
from utils import get_questions
from utils import get_result

MBTI_BP = Blueprint('mbti', __name__)
QUESTIONS = get_questions()

@MBTI_BP.route('/')
@MBTI_BP.route('/welcome/')
def welcome():
    '''欢迎页面，纯属装逼'''
    return render_template('mbti/welcome.html')


@MBTI_BP.route('/home/')
def home():
    '''尼玛逼这才是真正的首页啊'''
    return render_template('mbti/home.html')


@MBTI_BP.route('/about/')
def about():
    '''关于页面'''
    return render_template('mbti/about.html')


@MBTI_BP.route('/personalities/', defaults={'page': 'index'})
@MBTI_BP.route('/personalities/<page>/')
def personalities(page):
    '''SHOW MBTI TYPES'''
    try:
        return render_template('mbti/personalities/%s.html' % page)
    except:
        abort(404)


@MBTI_BP.route('/test/', methods=('GET', 'POST'))
def test():
    '''测试页面视图'''

    return render_template('mbti/test.html', questions=QUESTIONS)
