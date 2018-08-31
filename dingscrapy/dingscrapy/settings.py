# -*- coding: utf-8 -*-

BOT_NAME = 'dingscrapy'

SPIDER_MODULES = ['dingscrapy.spiders']
NEWSPIDER_MODULE = 'dingscrapy.spiders'

# 配置 user-agent，一般在headers中配置就可以了
# USER_AGENT = 'scrapy180402 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



ITEMS_SAVE_FILE = 'dingdian01.txt'

# 配置的线程数！ 默认是16个！
# CONCURRENT_REQUESTS = 32


# 每次下载后的 延时 ,单位是秒 , 默认是不延时
# 延时时间是  3*0.5 到 3*1.5 之间 随机获取
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 每一个域名的线程数
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 每一个服务器ip的线程数
# CONCURRENT_REQUESTS_PER_IP = 16
# 处理 结构化数据 item 的线程数
# CONCURRENT_ITEMS = 10


# 是否启用 cookie  ，默认是启用的， 一般不会配置为 False
# COOKIES_ENABLED = False

# 这个使用不上，控制台
#TELNETCONSOLE_ENABLED = False
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# 默认使用的 headers， 必须配置！！！
DEFAULT_REQUEST_HEADERS = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# 配置 爬虫中间层 ， 优先级 1-1000的范围， 数字越小，优先级越高
#SPIDER_MIDDLEWARES = {
#    'scrapy180402.middlewares.Scrapy180402SpiderMiddleware': 543,
#}

# 配置 下载器的中间层
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy180402.middlewares.Scrapy180402DownloaderMiddleware': 543,
#}


# 配置 结构化数据持久化 的操作类
ITEM_PIPELINES = {
   # 'dingscrapy.pipelines.dingscrapyPipeline': 100,
   'dingscrapy.pipelines.DingscrapyPipeline': 200,
}
# mysql数据库的配置
MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'db': 'dingdian20180720',
    'charset': 'utf8'
}




# 自动化处理的配置，使用 默认值配置就可以了
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 缓存的配置， 在测试环境下，可以开启，但是部署后一定要关闭！！！
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 默认是自动开启了日志的， 在控制台输出，如果要配置日子写在文件中，做以下配置
# 一旦配置了 日志写到文件，就不会在 控制台输出
# LOG_ENABLED = True

# LOG_FILE = 'log.txt'

# 日志记录的级别， 默认是 DEBUG
# 开发时，使用 debug 就可以了， 部署后使用 warning 或 error
LOG_LEVEL = 'DEBUG'