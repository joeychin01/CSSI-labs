import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_credentials_manager = SpotifyClientCredentials(client_id='a3af3476e5f24441ba77767bdd13f518', client_secret='08aee8a23fd148f3a790fe4116edecb1')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('joeychin01')

uri = playlists['items'][1]['uri']
tracks = sp.user_playlist_tracks('joeychin01', uri)['items']
for track in tracks:
    print(track['track']['name'])



# for playlist in playlists['items']:
#     print(playlist['uri'])
#
# tracks = sp.user_playlist_tracks()
#
# print(tracks)
