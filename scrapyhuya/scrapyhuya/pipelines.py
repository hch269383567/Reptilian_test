# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from db.mysql_handle import MysqlHandler


class ScrapyhuyaPipeline(object):
    def open_spider(self, spider):
        """
            spider 启动时，实例化一个 数据库操作类
        :param spider:
        :return:
        """
        # 从 settings 中 获取 mysql数据库的配置，key是：MYSQL_CONFIG
        mysql_config = spider.settings['MYSQL_CONFIG']
        mysql_handler = MysqlHandler(mysql_config)
        self.mysql_handler = mysql_handler

    def close_spider(self, spider):
        """
            spider关闭时， 关闭 数据库操作类

        :param spider:
        :return:
        """
        try:
            # 关闭数据库连接
            self.mysql_handler.dispose()
        except:
            print('关闭数据库连接失败！！！！！！！！！！')

    def process_item(self, item, spider):

        # with open('dingdian.txt', 'a', encoding='utf-8') as f:
        #     f.write(str(dict(item)))
        #     f.write('\n')

        # 插入一条记录
        self.mysql_handler.insertOne(
            'insert into huya1(name, biaoti, fangjianhao, game, hot,fans) values(%s, %s, %s, %s, %s,%s)',
            (item['name'], item['biaoti'], item['fangjianhao'], item['game'], item['hot'], item['fans']))
        # commit 提交
        self.mysql_handler.end()

        return item

