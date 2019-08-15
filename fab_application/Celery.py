from __future__ import absolute_import
from celery import Celery
app = Celery('my_celery')
# 加载配置模块
app.config_from_object('celeryconfig')

if __name__ == '__main__':
      app.start()
