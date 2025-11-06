import redis
from .config import settings

# 创建Redis连接池
redis_pool = redis.ConnectionPool.from_url(settings.redis_url)

# 创建Redis客户端
def get_redis():
    """获取Redis连接"""
    return redis.Redis(connection_pool=redis_pool)

# Redis键前缀
class RedisKeys:
    USER_SESSION = "user:session:{}"
    DEVICE_STATUS = "device:status:{}"
    API_RATE_LIMIT = "api:rate_limit:{}"
    MAINTENANCE_QUEUE = "maintenance:queue"