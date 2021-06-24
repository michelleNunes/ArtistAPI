import json
import lyricsgenius as genius

from flask import Flask

from services.constants import APIConstants
from services.database import Database

app = Flask(__name__)


@app.route("/music/<artista>/<cache>")
def get_artist_song(artista, cache=None):
    api = genius.Genius(APIConstants.GENIUS_TOKEN)

    artist = api.search_artist(artista, max_songs=10, sort="title")

    Database(artist, cache)

    return artist.songs


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
