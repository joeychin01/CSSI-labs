#main.py
# the import section
import webapp2
import jinja2
import os
from models import Meme
from google.appengine.api import urlfetch
import json
import random
random.seed()
#initializing jinja
#same on every main.py that uses jinja
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        api_url = "https://api.imgflip.com/get_memes"
        imgflip_response_json = urlfetch.fetch(api_url).content
        imgflip_response = json.loads(imgflip_response_json)
        print(imgflip_response['data']['memes'])
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        meme_templates = []
        memeTimes = 0
        for dict in imgflip_response['data']['memes']:
            if (random.random() * 10) < 1 and memeTimes < 8:
                meme_templates.append(dict['url'])
                memeTimes = memeTimes + 1
        meme_dict = {
            "imgs": meme_templates
        }
        self.response.write(welcome_template.render(meme_dict))

class ResultPage(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        top_line = self.request.get("top-line")
        bottom_line = self.request.get("bottom-line")
        meme_url = self.request.get("template")
        data_dict = {
            "top_line": top_line,
            "bottom_line": bottom_line,
            "url": meme_url
        }
        meme1 = Meme(first_line = data_dict["top_line"], second_line = data_dict["bottom_line"], pic_type = data_dict["url"])
        meme1.put()
        result_template = the_jinja_env.get_template('templates/result.html')
        self.response.write(result_template.render(data_dict))

class AllMemes(webapp2.RequestHandler):
    def get(self):
        all_memes = the_jinja_env.get_template('templates/allmemes.html')
        memes = Meme.query()
        memes_list = list(Meme.query().fetch())
        memes_dict = {"memes": memes_list}
        self.response.write(all_memes.render(memes_dict))



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/all-memes', AllMemes),
    ('/result', ResultPage)
], debug=True)
