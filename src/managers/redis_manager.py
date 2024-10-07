import time
import redis

from src.config import config


class RedisManager:
    def __init__(self) -> None:
        self._redis_manager = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    def add(self, key: str, value: str) -> None:
        now = int(time.time())
        key = f"{key}:{now}"
        self._redis_manager.set(key, value)
        self._redis_manager.expire(key, config.CF_TOKEN_EXP_SECONDS)

    def get(self, key: str) -> str | None:
        by_ = f"{key}:*"
        keys = self._redis_manager.scan(match=by_)[1]
        if not key:
            return

        ttl_list = [(key, self._redis_manager.ttl(key)) for key in keys]
        sorted_keys = sorted(ttl_list, key=lambda x: x[1])
        if not sorted_keys:
            return None
        name = (sorted_keys[0][0])
        print(name)
        oldest_token = self._redis_manager.get(name)
        self._redis_manager.delete(name)
        return oldest_token

redis_manager = RedisManager()
