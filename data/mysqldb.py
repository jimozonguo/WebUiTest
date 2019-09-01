#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from utils.config import Config


class MysqlData:
    """获取数据库数据的工具类"""
    def __init__(self):
        """读取配置文件数据源的配置"""
        self.dataConfig = Config().get('database')

    def connect_mysql(self):
        """
        连接到mysql数据库
        :return: 返回连接
        """
        db_config = dict(host=self.dataConfig["host"], port=self.dataConfig["port"], db=self.dataConfig["db"],
                         charset=str(self.dataConfig["charset"]), user=self.dataConfig["user"], passwd=str(self.dataConfig["password"]))
        try:
            cnx = pymysql.connect(**db_config)
        except Exception as err:
            raise err
        return cnx

    def executeSql(self, sql):
        """
        执行sql语句
        :param sql: sql字符串
        :return: 返回数据
        """
        cnx = self.connect_mysql()  # 连接mysql
        cns = cnx.cursor()  # 创建一个游标对象
        try:
            cns.execute(sql)
            re = cns.fetchall()
            cns.close()
        except Exception as err:
            cns.close()
            raise err
        return re

if __name__ == "__main__":
    s = MysqlData().executeSql(r"SELECT * FROM `case`;")
    print(s)