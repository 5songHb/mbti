#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import os
from collections import Counter
from more_itertools import flatten

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_questions():
    '''获取题目'''
    data_path = os.path.join(ROOT_PATH, 'data')
    question_txt = os.path.join(data_path, 'questions.txt')
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
    result = ''.join(t1 if answers.get(t1, 0) > answers.get(t2, 0) else
                     '({}/{})'.format(t1, t2) if answers.get(t1, 0) == answers.get(t2, 0) else t2
                     for t1, t2 in types)
    return result


if __name__ == '__main__':
    assert 'ISFP' == get_result(['I', 'S', 'F', 'P'])
    assert len(get_questions()) == 72
