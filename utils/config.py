#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from utils.file_reader import YamlReader

# 也建议大家多用os.path.split()和os.path.join(),可以支持linux和windows等不同的平台
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers', 'common')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
PAGEEL_PATH = os.path.join(BASE_PATH, 'pageel')


class Config:
    def __init__(self, config=CONFIG_FILE):
        print('配置文件地址：', config)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

if __name__=="__main__":
    url = Config().get('report')
    print(url["file_name"])
