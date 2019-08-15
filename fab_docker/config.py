from configparser import ConfigParser
import json
config = ConfigParser()
config.read('./conf.yml')  # ['conf.ini'] ['conf.cfg]


# 获取所有的section
# print(config.sections())  # ['mysql', redis]

conf_list = list()
for host in config.options('server'):
    str_host = config.get('server', host)
    json_host = json.loads(str_host)
    conf_list.append(json_host)


print(conf_list)
# conf = {}
# conf["server1_host"]  =  config.get('server', 'aliyun1_host')
# conf["server2_host"]  =  config.get('server', 'aliyun2_host')
# conf["server1_pwd"]  =  config.get('server', 'aliyun1_pwd')
# conf["server2_pwd"]  =  config.get('server', 'aliyun2_pwd')
# conf["server1_port"]  =  config.get('server', 'aliyun1_port')
# conf["server2_port"]  =  config.get('server', 'aliyun2_port')


# print(config.options('mysql'))
# print(config.options('redis'))


# mysql_host = config.get('mysql', 'host')           # 192.168.127.210
# redis_port = config.getint('redis', 'port')
# print(type(mysql_host))
# print(type(redis_port))




# config.items('mysql')
# config.items('redis')
# dict(config.items('redis'))




# def mysql():
#     config = ConfigParser()
#     config.read('./conf.yml')
#     section = 'mysql'
#     conf = {
#         'host': config.get(section, 'host'),
#         'port': config.getint(section, 'port'),
#         'user': config.get(section, 'user'),
#         'passwd': config.get(section, 'passwd'),
#         'db': config.get(section, 'db'),
#         'charset': config.get(section, 'charset')
#     }
#     # conn = pymysql.connect(**conf)
#     return conf

# import pymongo
# def mongodb():
#     config = ConfigParser()
#     config.read('./conf.yml')
#     section = 'mongodb'
#     conf = {
#         'host': config.get(section, 'host'),
#         'port': config.getint(section, 'port')
#         # 'db': config.get(section, 'db')
#     }
#     conn = pymongo.MongoClient(**conf)
#     db = conn[config.get(section, 'db')]
#     sheet = db["qxb"]
#     return [i for i in sheet.find({}).limit(3)]

# print(mongodb())
