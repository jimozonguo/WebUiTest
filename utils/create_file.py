#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

# 获得当前系统时间的字符串
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# 系统当前时间年份
year = time.strftime('%Y', time.localtime(time.time()))
# 月份
month = time.strftime('%m', time.localtime(time.time()))
# 日期
day = time.strftime('%d', time.localtime(time.time()))
# 小时
hour=time.strftime('%H', time.localtime(time.time()))
# 分钟
minute = time.strftime('%M', time.localtime(time.time()))
# 秒
second = time.strftime('%S', time.localtime(time.time()))

fileYear = '../report/'+'/'+year
fileMonth = fileYear+'/'+month
fileDay = fileMonth+'/'+day


def getFileName():
    if not os.path.exists(fileYear):
        os.mkdir(fileYear)
        os.mkdir(fileMonth)
        os.mkdir(fileDay)
    else:
        if not os.path.exists(fileMonth):
            os.mkdir(fileMonth)
            os.mkdir(fileDay)
        else:
            if not os.path.exists(fileDay):
                os.mkdir(fileDay)
    return fileDay


def getReportNmae():
    return year+month+day+hour+minute+second
