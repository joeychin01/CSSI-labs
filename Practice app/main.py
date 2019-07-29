#main.py
# the import section
import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='a3af3476e5f24441ba77767bdd13f518',
                                                              client_secret='08aee8a23fd148f3a790fe4116edecb1')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self): #for a get request
        if len(sys.argv) > 1:
            name = ' '.join(sys.argv[1:])
        else:
            name = 'Radiohead'
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            print(artist['name'], artist['images'][0]['url'])

        home_template = the_jinja_env.get_template('/templates/home.html')
        self.response.write(home_template.render())

class InputPage(webapp2.RequestHandler):
    def get(self):
        input_template = the_jinja_env.get_template('/templates/inputlyrics.html')
        self.response.write(input_template.render())
    def post(self):
        api_url = "https://orion.apiseeds.com/api/music/"
        api_url += self.request.get("artist_name") + "/"
        api_url += self.request.get("song_name")
        api_url += "?apikey=VHl5WJoexxSgghXe4zUdqAjrfSfOdbZjCGb6BkrODi5qquF3MFPGzNrFQr1Zsj4W"
        apiseeds_response = urlfetch.fetch(api_url)
        print(apiseeds_response)

class SpotifyPage(webapp2.RequestHandler):
    def get(self):
        import spotipy
        spotify = spotipy.Spotify()
        name = "john williams"
        results = spotify.search(q='artist:' + name, type='artist')
        print results
        spotify_template = the_jinja_env.get_template('/templates/spotifylyrics.html')
        self.response.write(spotify_template.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/inputlyrics', InputPage),
    ('/spotifylyrics', SpotifyPage),
    # ('/popularsearch', PopularPage)
], debug=True)
