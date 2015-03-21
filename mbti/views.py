#-*- coding:utf-8 -*-
from flask import render_template
from flask import Blueprint

MBTI_BP = Blueprint('mbti', __name__)

@MBTI_BP.route('/')
def home():
    return render_template('mbti/home.html')


@MBTI_BP.route('/test')
def test():
    return render_template('mbti/test.html')
