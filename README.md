# Fab
基于python第三方库 fabric 实现远程ssh分布式调度部署应用, 这里接入了Celery分布式队列，使用docker环境打包应用服务
这样在多台服务器下，不管是不是docker环境，都可以达到一键部署的效果，还是威力十足的。
