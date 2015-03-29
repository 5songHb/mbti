#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import os
from collections import Counter
from more_itertools import flatten

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(ROOT_PATH, 'data')


def get_questions():
    '''获取题目'''
    question_txt = os.path.join(DATA_PATH, 'questions.txt')
    questions = []
    with open(question_txt) as txt:
        for line in txt:
            question, choice_a, choice_b = line.decode('utf-8').split()
            questions.append({
                'question': question,
                'choice_a': {'value': choice_a[-1], 'text': choice_a[:-1]},
                'choice_b': {'value': choice_b[-1], 'text': choice_b[:-1]}
            })
    return questions


def get_result(answers):
    '''计算测试结果
    E-I S-N T-F J-P
    '''
    types = [('E', 'I'), ('S', 'N'), ('T', 'F'), ('J', 'P')]
    answers = Counter(answers)
    if set(answers.keys()) - set(flatten(types)):
        raise Exception('TypesError', 'answer type is not in types')
    result = ''.join(t1 if answers.get(t1, 0) > answers.get(t2, 0) else t2
                     for t1, t2 in types)
    return result


def get_types_desc():
    '''十六种人格简要描述'''
    types_txt = os.path.join(DATA_PATH, 'types_desc.txt')
    types_desc = {}
    with open(types_txt) as types:
        for line in types:
            typ3, desc = line.decode('utf-8').split()
            types_desc[typ3] = desc
    return sorted(types_desc.items(), key=lambda i: i[0])

if __name__ == '__main__':
    assert 'ISFP' == get_result(['I', 'S', 'F', 'P'])
    assert len(get_questions()) == 72
    assert len(get_types_desc()) == 16
