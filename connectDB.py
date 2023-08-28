#_*_ coding:utf-8 _*_

import os
from tkinter import *

try:
    import pymysql
    import pandas as pd
    import base64
    from PIL import Image
    from io import BytesIO
except ImportError:
    os.system('pip install pymysql')
    os.system('pip install pandas')
    os.system('pip install pillow')
    os.system('pip install base64')
    os.system('pip install BytesIO')

### MYSQL 연결###

try:
    conn = pymysql.connect(host='13.209.97.12',
                           port=57598,
                           user='kangjeseong',
                           password='ansan',
                           db='com3101',
                           charset='utf8')
    db_info = conn.get_server_info()
    print('mysql version : ', db_info)
    cur = conn.cursor()
except Exception as e:
    print('mysql error : ', e)
