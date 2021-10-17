import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Metadata():
    def __init__(self, title, artists, image):
        self.title = title
        self.artists = artists
        self.image = image

    def __str__(self):
        return f'Title: {self.title}\nArtists: {self.artists}'


class Client():
    def __init__(self, scope, id, secret, uri):
        self.scope = scope
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=self.scope, client_id=id, client_secret=secret, redirect_uri=uri))

    def get_current(self) -> Metadata:
        current = self.sp.current_user_playing_track()
        if current == None:
            return Metadata('', '', '')
        raw = current['item']
        title = raw['name']
        artists = list(map(lambda x: x['name'], raw['artists']))
        image = raw['album']['images'][0]['url']
        return Metadata(title, artists, image)


if __name__ == '__main__':
    scope = 'user-read-currently-playing'
    c = Client(scope)
    print(c.get_current())
