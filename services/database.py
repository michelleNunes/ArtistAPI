import json
import uuid
from services.redislib import RedisManager
from services.constants import APIConstants
from services.dyanamolib import DynamoLib


def Database(artist_information, cache: bool):
    database_artist = redis_information(artist_information, cache)

    return database_artist


def redis_information(artist_information, cache):
    """"
        Save all artist information
        :param artist_information: all artist songs
        :param cache: False: to delete the information, True: to use redis information
        :return: The 10 songs
    """
    artist_name = artist_information.name

    if cache == "false":
        RedisManager.delete_key(artist_name)
        DynamoLib.delete_item(artist_name)

    information = create_artist_information(artist_name, artist_information)
    redis_info = RedisManager.get(artist_name)

    if redis_info:
        return json.loads(redis_info)
    else:
        RedisManager.set(artist_name, json.dumps(information))
        save_database(artist_name, information)
        return information


def save_database(artist_name, artist_information):
    uuid_info = str(uuid.uuid4())
    DynamoLib.create_item(uuid_info, artist_name, artist_information)


def create_artist_information(artist_name, artist_information):
    information = {}
    artist_information_songs = artist_information.songs
    for songs_data in artist_information_songs:
        if artist_name not in information:
            information[artist_name] = {
                APIConstants.SONGS: []
            }
        song_name = songs_data.title
        information[artist_name][APIConstants.SONGS].append(song_name)

    return information
