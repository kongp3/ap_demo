# -*- coding: utf-8 -*-
import urllib
from flask import Flask

# 应用服务器配置
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app_host = '0.0.0.0'
app_port = 31082

WEB_HOST = 'http://0.0.0.0:31082/'


MYSQL_HOST = '0.0.0.0'
MYSQL_PASS = 'XXXXXXX'
MYSQL_USER = 'root'


MYSQL_CONN = 'mysql+mysqldb://{0}:{1}@{2}/audit-pioneer?charset=utf8'.format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
