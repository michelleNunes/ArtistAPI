from redis import Redis, exceptions
from typing import Final


class RedisManager(object):
    try:
        instance = Redis(host='localhost', port=6379)
        instance.ping()
    except (ConnectionError, exceptions.ConnectionError):
        print("Using Redis from localhost")

    __instance: Final[Redis] = instance

    @staticmethod
    def get(name: str):
        return RedisManager.__instance.get(name)

    @staticmethod
    def set(name: str, value: str):
        return RedisManager.__instance.setex(name, 604800, value)

    @staticmethod
    def delete_key(name: str):
        keys = RedisManager.__instance.keys(f"{name}*")
        return RedisManager.__instance.delete(*keys) if keys else None
