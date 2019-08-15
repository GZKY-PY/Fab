FROM python:3.6
RUN mkdir /celery_app
WORKDIR /celery_app
COPY . /celery_app/
RUN pip install -r requirements.txt

# RUN celery -A Celery worker -l info
