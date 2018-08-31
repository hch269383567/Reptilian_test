#!/usr/bin/env python
# -*- coding: utf-8 -*-
from douyu1scrapy.spiders.douyu import Douyu1Spider

__author__ = 'Terry'


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider
process.crawl(Douyu1Spider)

# 启动爬虫，会阻塞，直到爬取完成
process.start()
