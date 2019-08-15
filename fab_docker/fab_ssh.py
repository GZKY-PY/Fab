
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
        # env.hosts=[host]
        # env.password=pwd
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

    # def Hide_all(self):
    #     with settings(hide('everything'), warn_only=True):  # 关闭显示
    #         result = run('ls')
    #         print(result)  # 命令执行的结果
    #         print(result.return_code)

    # def Show_all(self):
    #     with settings(show('everything'), warn_only=True):  # 显示所有
    #         result = run('docker')
    #         print(str(result.return_code))  # 返回码，0表示正确执行，1表示错误
    #         print(str(result.failed))

    # @task
    # def Prefix(self): # 前缀，它接受一个命令作为参数，表示在其内部执行的代码块，都要先执行prefix的命令参数。
    #     with cd('../home'):
    #         with prefix('echo 123'):
    #             run('echo caonima')


    # def Shell_env(self): # 设置shell脚本的环境变量　
    #     with shell_env(HTTP_PROXY='1.1.1.1'):
    #         run('echo $HTTP_PROXY')


    # def Path_env(self): # 配置远程服务器PATH环境变量，只对当前会话有效，不会影响远程服务器的其他操作，path的修改支持多种模式
    #     with path('/tmp', 'prepend'):
    #         run("echo $PATH")
    #     run("echo $PATH")


    # def Mongo(self): # 尝试连接mongodb数据库  不知道为什么制定端口就不行了
    #     # with remote_tunnel(27017):
    #     run('mongo')


    # def Mysql(self):  # 尝试连接mysql数据库
    #     with remote_tunnel(3306):
    #         run('mysql -u root -p password')

    '''
    指定host时，可以同时指定用户名和端口号： username@hostname:port
    通过命令行指定要多哪些hosts执行人物：fab mytask:hosts="host1;host2"
    通过hosts装饰器指定要对哪些hosts执行当前task
    通过env.reject_unkown_hosts控制未知host的行为，默认True，类似于SSH的StrictHostKeyChecking的选项设置为no，不进行公钥确认。
    '''

    # @hosts('root@ip:22')
    # @task
    # def Get_Ip(self):
    #     run('ifconfig') 
    #     # return run("ip a")

    # @hosts("root@ip:22")
    # @runs_once
    # def Get_One_Ip(self):
    #     run('ifconfig')

    '''
    role是对服务器进行分类的手段，通过role可以定义服务器的角色，
    以便对不同的服务器执行不同的操作，Role逻辑上将服务器进行了分类，
    分类以后，我们可以对某一类服务器指定一个role名即可。
    进行task任务时，对role进行控制。
    '''

    # @roles('web')  # 只对role为db的主机进行操作
    # @task
    # def Roles_Get_Ip():
    #     run('ifconfig')
        

    # def Confirm(self): # 有时候我们在某一步执行错误，会给用户提示，是否继续执行时，confirm就非常有用了，它包含在 fabric.contrib.console中
    #     result = confirm('Continue Anyway?')
    #     print(result)

    # def run_python(self):
    #     run("python3 trigger.py")

    @task
    @parallel
    def celery_call(): # 执行celery任务
        with cd('../home'):
            warn(yellow('----->Celery'))
            puts(green('----->puts'))
            run('cd ./celery_1 && celery -A Celery worker -l info')
            time.sleep(3)
            run('python3 run_tasks.py')
    

    # @task
    # def update_file(): # 上传文件到服务器
    #     with settings(warn_only=True):
    #         local("tar -czf test.tar.gz config.py")
    #         result = put("test.tar.gz", "/home/test.tar.gz")
    #     if result.failed and not confirm("continue[y/n]?"):
    #         abort("put test.tar.gz failed")

    #     with settings(warn_only=True):
    #         local_file_md5 = local("md5sum test.tar.gz",capture=True).split(" ")[0]
    #         remote_file_md5 = run("md5sum /home/test.tar.gz").split(" ")[0]
    #     if local_file_md5 == remote_file_md5:
    #         print(green("local_file == remote_file"))
    #     else:
    #         print(red("local_file != remote"))
    #     run("mkdir /home/test")
    #     run("tar -zxf /home/test.tar.gz -C /home/scp")

    '''
    有一个地方很神奇，self和@task装饰器在类中不能共用，否则会报错
    '''

    # @task
    # def downloads_file(): # get文件到本地
    #     with settings(warn_only=True):
    #         result = get("/home/celery_1", "./")
    #     if result.failed and not confirm("continue[y/n]?"):
    #         abort("get test.tar.gz failed")
    #     local("mkdir ./test")
    #     local("tar zxf ./hh.tar.gz -C ./test")

    # @task
    # @parallel
    # def scp_docker_file():
    #     with settings(warn_only=True):
    #         local("tar -czf docker.tar.gz ../docker")
    #         result = put("docker.tar.gz", "/home/docker.tar.gz")
    #     if result.failed and not confirm("continue[y/n]?"):
    #         abort("put dockerfile failed")
    #     run("mkdir /home/docker")
    #     run("tar -zxf /home/docker.tar.gz -C /home")


    def Run(self):
        execute(self.celery_call)
    

h = HA()
h.Run()


