
import warnings
warnings.filterwarnings("ignore")
import time
from fabric.api import * # run,cd,env,hosts,execute,sudo,settings,hide
from fabric.colors import *
from fabric.contrib.console import confirm
import config
import json
from fabric.tasks import Task


class HA():
    def __init__(self):
        self.host = "root@{host}:{port}"
        self.ssh = "root@{host}:{port}"
        self.env = env
        self.env.warn_only = True # 这样写比较痛快
        self.env.hosts = [
            self.host.format(host=host[0],port=host[2]) for host in config.conf_list]
        self.env.passwords = {
            self.ssh.format(host=host[0], port=host[2]):host[1] for host in config.conf_list}

        # self.env.roledefs = {
        #     'web': [self.env["hosts"][0]],  # role名称为：web
        #     'db': [self.env["hosts"][1] ]  # role名称为：db
        # }

        print(self.env["hosts"])

    
    
    @task
    def get_docker_v(): # 查看docker版本
        with cd('../home'):
            run('docker version')

    @task
    def pull_images(images_name):
        with settings(warn_only=True):
            with cd("../home/"):
                try:
                    run("docker pull {}".format(images_name))
                except:
                    abort("docker pull failed")

    @task
    def push_images(images_name,username_repository,tag):
        with settings(warn_only=True):
            with cd("../home/"):
                try:
                    run("docker tag {image_name} {username_repository}:{tag}".format(images_name=images_name,username_repository=username_repository,tag=tag))
                    run("docker push {username_repository}:{tag}".format(username_repository=username_repository,tag=tag))
                except:
                    abort("docker push failed")

    @task
    def run_docker_images(images_name_tag):
        with settings(warn_only=True):
            with cd("../home/"):
                try:
                    run("docker run -p 4000:80 {}".format(images_name_tag))
                except:
                    abort("docker run failed")


    @task
    @parallel
    def execute_docker_compose():
        with settings(warn_only=True):
            with cd("../home/flask_app"):
                run("docker-compose up")


    @task
    def create_docker_service(service_name,images_name,num=4):
        with settings(warn_only=True):
            with cd("../home/"):
                run("docker service create --name {service_name} -p 4000:80 {images_name}".format(service_name=service_name,images_name=images_name))
                run("docker service scale {service_name}={num}".format(service_name=service_name,num=num))
    
    
    @task
    def stop_docker_service(service_name):
        with settings(warn_only=True):
            with cd("../home/"):
                run("docker service rm {}".format(service_name))

    def Run(self):
        # execute(self.create_docker_service,"demo","3417947630/py:hello")
        execute(self.execute_docker_compose)

h = HA()
h.Run()
