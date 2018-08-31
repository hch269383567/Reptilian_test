import redis

#直接创建数据库 ，会自动使用连接池
#设置为True 写入值为str
r=redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)