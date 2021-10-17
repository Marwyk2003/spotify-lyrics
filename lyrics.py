import requests


class Lyrics():
    def __init__(self, title, artists):
        self.title = title
        self.artists = artists

    def get_lyrics(self):
        for artist in self.artists:
            response = requests.get(
                f'https://api.lyrics.ovh/v1/{artist}/{self.title}')
            if (response.status_code == 404):
                continue
            lyrics = response.json()['lyrics']
            # remove the first line (title and artists)
            lyrics = lyrics.split("\n", 1)[1]
            return lyrics
        return 'Failed to get lyrics'

    def get_lyrics_array(self):
        lyrics = self.get_lyrics()
        return list(map(lambda x: x.split('\n'), lyrics.split('\n\n')))


if __name__ == '__main__':
    lyrics = Lyrics('Time', ['Pink Floyd'])
    print(lyrics.get_lyrics())
