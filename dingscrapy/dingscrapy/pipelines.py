# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from db.mysql_handle import MysqlHandler


class dingscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class DingscrapyPipeline(object):
    def process_item(self, item, spider):
        item['book_name'] = item['book_name']
        item['zz'] = item['zz']
        item['gx'] = item['gx']
        item['zs'] = item['zs']
        return item

    class DingscrapyPipeline(object):

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
                'insert into dingdian(book_name, zz, zs, gx) values(%s, %s, %s, %s)',
                (item['book_name'], item['zz'], item['zs'], item['gx'],))
            # commit 提交
            self.mysql_handler.end()

            return item

    #     if item:
    #         # 是在settings中配置 的 保存文件的名字！
    #         file = spider.settings['ITEMS_SAVE_FILE']
    #
    #         with open('file', 'a', encoding='utf-8') as f:
    #             f.write('-----'.join([item['book_name'], item['zz'], item['gx'],item['zs'], '\n']))
    #     # print(item['book_name'],item['zz'])
    #         # 将 item 传递给下一个 pipeline， 如果是最后一个 pipeline了，那么这个调用不起作用
    #     return item