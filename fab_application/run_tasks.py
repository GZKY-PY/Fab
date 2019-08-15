# -*-coding:UTF-8-*-
from __future__ import absolute_import
from tasks import add, max, send_weixin, x3
from celery import group

#调用任务会返回一个 AsyncResult 实例，可用于检查任务的状态，等待任务完成或获取返回值（如果任务失败，则为异常和回溯）。
#但这个功能默认是不开启的，你需要设置一个 Celery 的结果后端(即backen，我们在tasks.py中已经设置了，backen就是用来存储我们的计算结果)
result1 = add.delay(10, 1000)
result2 = max.delay(3000,600)
result3 = x3.delay(10,1000,100)
result4 = send_weixin.delay("微信通知ID")

# if (result1.ready()):
#   # 获取任务执行结果
#   print(result1.get(timeout=1))

# if (result2.ready()):
#   # 获取任务执行结果
#   print(result2.get(timeout=1))

#if (result3.ready()):
  # 获取任务执行结果
 # print(result3.get(timeout=1))

# from datetime import datetime, timedelta
# tomorrow = datetime.utcnow() + timedelta(seconds=3)
# add.apply_async((2, 2), eta=tomorrow)
# result = add.apply_async((2, 2), countdown=3)

# add_group = group(add.s(i, i) for i in range(10))
# result = add_group.delay()
# print(result.get())
