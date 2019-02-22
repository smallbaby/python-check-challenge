# -*- coding:utf8 -*-

import os
import time
import sys
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header


msg_from = '328832654@qq.com'
passwd = 'nexwymerqxxnxxxdhbjef' # 授权码（qq邮箱需要申请授权码，别的邮箱应该是密码）
msg_to = '328832654@qq.com'


class Weather(object):
    def __int__(self):
        self.url = '彩云天气Token正在申请中'
        self.token = ''
        self.data = None


    def send_msg(self):

        subject = self.data  # 主题
        content = self.data
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")
        except Exception as e:
            print("发送失败"+e)
        finally:
            s.quit()

    def get_weather(self):
        '''
        get current time weather
        :return: json
        '''
        content = requests.get(self.url)
        if content:
            self.data = content

if __name__ == '__main__':
    w = Weather()
    w.get_weather()
    w.send_msg()