# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/08/28
# Desc:

"""
1、生成试卷
2、生成自测题目
"""

URL = 'http://localhost:8088/api/exam'

data = {"source": "保存测试", "description": "保存测试", "institute": "税务", "major": "税务", "grade": "2021",
        "examDate": "2021-10-01", "totalTime": "120", "totalScore": "100", "type": "税务", "tips": '', "paperId": 1006}

_a = ['A', 'B', 'C', 'D']


def test():
    for x in range(10, 30):
        data['source'] = f'保存测试({x})'
        data['description'] = f'保存测试({x})'
        data['paperId'] = data['paperId'] + 1
        print(data)


def _h(_l, single=False, key='A'):
    x = None
    if _l.startswith(key):
        x = _l[1:]
    if single:
        try:
            pass
            # x = _l.split(key)[1].strip()
        except Exception as e:
            print("err", e)
    if _l.find('、') > -1:
        x = _l.split('、')[1].strip()
    if _l.find('正确答案') > -1:
        x = _l.split('正确答案')[1].strip()
    return x


def _h2(_l, single=False, key='A'):
    x = None
    if _l.startswith(key + '、'):
        x = _l[2:]
    elif _l.startswith(key):
        x = _l[1:]
    if single:
        try:
            pass
            # x = _l.split(key)[1].strip()
        except Exception as e:
            print("err", e)
    if _l.find('正确答案') > -1:
        x = _l.split('正确答案')[1].strip()
    return x


def _content(j, question, _l):
    if _l.find('单选题') > -1:
        return _l.split('单选题')[1].strip(), 1
    elif _l.find('、') > -1:
        return _l.split('、', 1)[1], 0
    return _l, 2


def _content2(j, question, _l):
    if _l.find('多选题') > -1:
        return _l.split('多选题')[1].strip(), 1
    # elif _l.find('、') > -1:
    #     return _l.split('、', 1)[1], 0
    return _l, 2


def main(file="exam1.txt"):
    """单选题"""
    f = open(file)
    x = -1
    j = 0
    single = False
    question = {}
    questions = []
    for _l in f.readlines():
        _l = _l.strip()
        x = x + 1
        if _l.find('6月29日“深入学习领会和贯彻落实新时代党的组织路线”第二十一次集体学习时，习近平总书记强调') > -1:
            pass
        if x == 0:
            try:
                question['content'], type = _content(j, question, _l)
                if type == 1:
                    single = True
            except:
                pass
        if x == 1:
            try:
                question['A'] = _h(_l, single, 'A')
                if not _h(_l, single, 'A'):
                    _h(_l, single, 'A')
            except:
                pass
        if x == 2:
            try:
                question['B'] = _h(_l, single, 'B')
            except:
                pass
        if x == 3:
            try:
                question['C'] = _h(_l, single, 'C')
            except:
                pass
        if x == 4:
            question['D'] = _h(_l, single, 'D')
        if x == 5:
            try:
                if single:
                    pass
                question['q'] = _l[_l.find('\t') + 1].strip() if _l and _l.find("\t") > 0 else _l
                question['q'] = question['q'].replace('（正确答案）', '') \
                    .replace('【正确】', '') \
                    .replace('【正确】', '') \
                    .replace('【答案】', '') \
                    .replace('答案', '').replace('正确：', '').replace('正确', '').replace('正常：', '').replace('【】',
                                                                                                       '').replace(',',
                                                                                                                   '')
                question['q'] = question['q'].strip()
                questions.append(question)
                single = False
            except:
                pass
            question = {}
            x = -1
            j += 1
            if j > 30000:
                break

    i = 0
    for q in questions:
        f = f'insert into multi_question(subject,question,answerA,answerB,answerC,answerD,' \
            f'rightAnswer,score,section, level) value("所有题目","{q["content"]}","{q["A"]}","{q["B"]}","{q["C"]}","{q["D"]}","{q["q"]}", 1, "税务",1);'
        print(f)


def multiple(file="exam2.txt"):
    """
    多选题
    :param file:
    :return:
    """
    f = open(file)
    x = -1
    j = 0
    single = False
    question = {}
    questions = []
    for _l in f.readlines():
        _l = _l.strip()
        x = x + 1
        if x == 0:
            try:
                question['content'], type = _content2(j, question, _l)
                question['content'] = question['content'].strip()
                if type == 1:
                    single = True
            except:
                pass
        if x == 1:
            try:
                question['A'] = _h2(_l, single, 'A')
            except:
                pass
        if x == 2:
            try:
                question['B'] = _h2(_l, single, 'B')
            except:
                pass
        if x == 3:
            try:
                question['C'] = _h2(_l, single, 'C')
            except:
                pass
        if x == 4:
            question['D'] = _h2(_l, single, 'D')
        if x == 5:
            try:
                if single:
                    pass
                question['q'] = _l
                question['q'] = question['q'].replace('（正确答案）', '') \
                    .replace('【正确】', '') \
                    .replace('【正确】', '') \
                    .replace('【答案】', '') \
                    .replace('答案', '').replace('.', '').replace('确认', '').replace('正确：', '').replace('正确', '').replace(
                    '正常：',
                    '').replace('【】',
                                '').replace(
                    ',',
                    '')
                question['q'] = question['q'].replace('、', ',').strip()
                if ',' not in question['q']:
                    question['q'] = ','.join([x for x in question['q']])
                questions.append(question)
                single = False
            except:
                pass
            question = {}
            x = -1
            j += 1
            if j > 30000:
                break

    i = 0
    for q in questions:
        i += 1
        f = f'insert into multi_question(subject,question,answerA,answerB,answerC,answerD,' \
            f'rightAnswer,score,section, level) value("所有题目","{q["content"]}","{q["A"]}","{q["B"]}","{q["C"]}","{q["D"]}","{q["q"]}", 1, "税务",1);'
        print(f)


def judge(file="judge.txt"):
    """
    判断题
    :param file:
    :return:
    """
    f = open(file)
    x = -1
    j = 0
    single = False
    question = {}
    questions = []
    for _l in f.readlines():
        _l = _l.strip()
        x = x + 1
        if x == 0:
            try:
                question['content'] = _l.strip()
            except:
                pass
        if x == 1:
            try:
                question['q'] = _l
                questions.append(question)
            except:
                pass
            question = {}
            x = -1
            j += 1
            if j > 30000:
                break

    for q in questions:
        f = f'insert into judge_question (subject,question,answer,score,level,section) value("所有题目", "{q["content"]}", "{"T" if q["q"] == "A" else "F"}", 1,1,"税务");'
        print(f)


def other(FILE="other.txt"):
    f = open(FILE)
    x = -1
    question = {}
    questions = []
    for _l in f.readlines():
        _l = _l.strip()
        x = x + 1
        if x == 0:
            question['content'] = _l.strip()
        if x == 1:
            question['A'] = _l.strip().replace('A、', '')
        if x == 2:
            question['B'] = _l.strip().replace('B、', '')
        if x == 3:
            question['C'] = _l.strip().replace('C、', '')
        if x == 4:
            question['D'] = _l.strip().replace('D、', '')
        if x == 5:
            question['q'] = _l.strip().replace('，', ',').replace('、', ',')
            questions.append(question)
            question = {}
            x = -1
    for q in questions:
        f = f'insert into multi_question(subject,question,answerA,answerB,answerC,answerD,' \
            f'rightAnswer,score,section, level) value("所有题目","{q["content"]}","{q["A"]}","{q["B"]}","{q["C"]}","{q["D"]}","{q["q"]}", 1, "税务",1);'
        print(f)


if __name__ == '__main__':
    main()
    multiple()
    judge()
    other()
