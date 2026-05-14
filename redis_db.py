import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Pool de conexão para o Redis
pool = redis.ConnectionPool(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    db=0, 
    decode_responses=True,
    max_connections=10
)

def get_redis():
    return redis.Redis(connection_pool=pool)
