# spotify-lyrics
## Instalation
Install requirements given in `requirements.txt`
```console
pip3 install -r requirements.txt
```
[Create a spotify application](https://developer.spotify.com/dashboard/applications)<br/>
Go to Edit settings and set the `Redirect URI` (e.g. http://127.0.0.1:PORT)<br/>
Copy `Client ID`, `Client Secret` and `Redirect URI` to `config.yml`

Use
```console
flask run
```
To run the applictaion. By default it runs on http://localhost:5000
