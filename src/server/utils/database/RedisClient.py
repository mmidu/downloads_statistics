import redis

class RedisClient:
    class __RedisClient:
        def __init__(self, host, port, db):
            self.client = redis.Redis(host='ds_redis', port=6379, db=0)
        def __str__(self):
            return repr(self) + self.client
    instance = None
    def __init__(self, host, port, db):
        if not RedisClient.instance:
            RedisClient.instance = RedisClient.__RedisClient(host, port, db)
        else:
            RedisClient.instance.client = redis.Redis(host='ds_redis', port=6379, db=0)
    def __getattr__(self, name):
        return getattr(self.instance, name)

Redis = RedisClient('ds_redis', 6379, 0)
