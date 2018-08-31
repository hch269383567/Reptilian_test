#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

__author__ = 'Terry'




'''
    这个MySQL封装类
'''

class MysqlHandler(object):
    def __init__(self, config):
        #数据库构造函数，从连接池中取出连接，并生成操作游标
        self.config = config

        self._conn = self.__getConn()
        self._cursor = self._conn.cursor()



    def __getConn(self):
        """
        @summary : 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """

        config = self.config

        # 将数据库的返回值设置为字典
        config['cursorclass'] = pymysql.cursors.DictCursor
        conn = pymysql.connect(**config)
        return conn

    def getAll(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result
        list(字典对象) / boolean
        查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count>0:
            result = self._cursor.fetchall()
        else:
            result = []
        return result

    def getOne(self,sql,param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]
        传递进来
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result
        list / boolean
        查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count>0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self,sql,num,param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组 / 列表）
        @return: result  list / boolean  查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count>0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertOne(self, sql, value):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的ＳＱＬ格式
        @param value:要插入的记录数据tuple / list
        @return: insertId 受影响的行数
        """
        self._cursor.execute(sql, value)
        return self.__getInsertId()

    def insertMany(self,sql,values):
        """
        @summary: 向数据表插入多条记录
        @paramsql:要插入的ＳＱＬ格式
        @paramvalues:要插入的记录数据tuple(tuple) / list[list]
        @return: count受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id, 如果没有则为０
        """
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']

    def __query(self,sql,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count

    def update(self,sql,param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用( % s, % s)
        @param param: 要更新的值  tuple / list
        @return: count 受影响的行数
        """
        return self.__query(sql,param)

    def delete(self,sql,param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用( % s, % s)
        @param param: 要删除的条件  值  tuple / list
        @return: count受影响的行数
        """
        return self.__query(sql,param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option=='commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd==1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()


def insert(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.insertOne(sql, params)
    finally:
        mysql.dispose()
    return ret

def insert_many(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.insertMany(sql, params)
    finally:
        mysql.dispose()
    return ret

def delete(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.delete(sql, params)
    finally:
        mysql.dispose()
    return ret

def update(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.update(sql, params)
    finally:
        mysql.dispose()
    return ret

def get_one(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.getOne(sql, params)
    finally:
        mysql.dispose()
    return ret

def get_many(sql, params=None, num=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.getMany(sql, num, params)
    finally:
        mysql.dispose()
    return ret

def get_all(sql, params=None):
    mysql = MysqlHandler()
    try:
        ret = mysql.getAll(sql, params)
    finally:
        mysql.dispose()
    return ret


if __name__ == '__main__':
    mysql_handler = MysqlHandler()
    r = mysql_handler.getOne('select * from dingdian')
    print(r)