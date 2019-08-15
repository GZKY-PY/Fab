# -*-coding:UTF-8-*-
from __future__ import absolute_import
import requests
from Celery import app

@app.task
def add(a, b):
  print("ADD TASK !!!")
  return a + b

@app.task
def max(x, y):
  print("MAX TASK !!!")
  return x * y

@app.task
def max3(x, y, z):
  print("MAX3 TASK !!!")
  return x * y * z

@app.task
def send_weixin(key):
    print("WEIXIN TASK !!!")
    url = "https://sc.ftqq.com/{key}.send".format(key=key)
    subject = "SEND TASK !!!"
    r = requests.post(url, data={"text": subject, "desp": "微信通知text"})
    if r.status_code == requests.codes.ok:
        return True
    else:
        return False
