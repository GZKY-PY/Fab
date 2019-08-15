from __future__ import absolute_import
import datetime
from kombu import Exchange, Queue
from celery.schedules import crontab
BROKER_URL = 'redis://127.0.0.1:6379/0'
# backen
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# 导入任务，如tasks.py
CELERY_IMPORTS = ('tasks', )
# 列化任务载荷的默认的序列化方式
CELERY_TASK_SERIALIZER = 'json'
# 结果序列化方式
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TIMEZONE='Asia/Shanghai'    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'
# CELERY_ENABLE_UTC = True

# 设置任务的优先级或任务每分钟最多执行次数
# CELERY_ROUTES = {
    # 如果设置了低优先级，则可能很久都没结果
    #'tasks.add': 'low-priority',
    #'tasks.add': {'rate_limit': '10/m'}，
    #'tasks.add': {'rate_limit': '10/s'}，
    #'*': {'rate_limit': '10/s'}
# }


# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'tasks.add',
         'schedule': datetime.timedelta(seconds=30),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'tasks.add',
        'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}


# borker池，默认是10
BROKER_POOL_LIMIT = 10
# 任务过期时间，单位为s，默认为一天
CELERY_TASK_RESULT_EXPIRES = 3600
# backen缓存结果的数目，默认5000
CELERY_MAX_CACHED_RESULTS = 10000


CELERY_QUEUES = (
Queue("default",Exchange("default"),routing_key="default"),
Queue("for_add",Exchange("for_add"),routing_key="for_add"),
Queue("for_max",Exchange("for_max"),routing_key="for_max"),
Queue("for_x3",Exchange("for_x3"),routing_key="for_x3"),
Queue("for_send_weixin",Exchange("for_send_weixin"),routing_key="for_send_weixin")
)
# 路由
CELERY_ROUTES = {
'tasks.add':{"queue":"for_add","routing_key":"for_add"},
'tasks.max':{"queue":"for_max","routing_key":"for_max"},
'tasks.x3':{"queue":"for_x3","routing_key":"for_x3"},
'tasks.send_weixin': {"queue":"for_send_weixin","routing_key":"for_send_weixin"}
}
