import json
import uuid
from services.redislib import RedisManager


def Database(artist_information, cache=None):
    artist_name = artist_information.name

    value = redis_information(artist_information, cache)

    return artist_information


def redis_information(artist_information, cache=None):
    artist_name = artist_information.name
    if cache:
        RedisManager.delete_key(artist_name)
    else:
        redis_info = RedisManager.get(artist_name)

        if redis_info:
            return json.loads(redis_info)
        else:
            RedisManager.set(artist_name, "test")
            save_database(artist_information)
            return True

def save_database(artist_information):
    artist_name = artist_information.name
    uuid_info = str(uuid.uuid4())

