import yaml
from flask import Flask, render_template
from spotify import Client
from lyrics import Lyrics

app = Flask(__name__)

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

spotify_credentials = cfg['spotify_credentials']
spotify_client = Client('user-read-currently-playing',
                        spotify_credentials['client_id'],
                        spotify_credentials['client_secret'],
                        spotify_credentials['redirect_uri'])


@app.route("/")
def index():
    metadata = spotify_client.get_current()
    lyrics = Lyrics(metadata.title, metadata.artists)
    content = lyrics.get_lyrics_array()
    return render_template('index.html', content=content, artists=''.join(metadata.artists), title=metadata.title, image=metadata.image)


@app.route("/<artist>/<title>")
def custom(artist, title):
    lyrics = Lyrics(title, [artist])
    content = lyrics.get_lyrics_array()
    return render_template('index.html', content=content, artists=artist, title=title, image='https://bulma.io/images/placeholders/128x128.png')
