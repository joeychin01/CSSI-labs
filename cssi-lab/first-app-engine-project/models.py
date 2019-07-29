from google.appengine.ext import ndb

class Meme(ndb.Model):
  first_line = ndb.StringProperty(required=True)
  second_line = ndb.StringProperty(required=False)
  pic_type = ndb.StringProperty(required=False)

  def get_meme_url(self):
    if self.pic_type == 'mocking_spongebob':
        url = 'https://i.imgflip.com/2/1otk96.jpg'
    elif self.pic_type == 'button':
        url = 'https://i.imgflip.com/2/1yxkcp.jpg'
    elif self.pic_type == 'roll-think':
        url = 'https://i.imgflip.com/2/1h7in3.jpg'
    elif self.pic_type == 'toy-story':
        url = 'https://i.imgflip.com/2/1ihzfe.jpg'
    elif sel.pic_type == 'me-boys':
        url = 'https://i.imgflip.com/2/320xfw.jpg'
    elif self.pic_type == 'one-simply':
        url = 'https://i.imgflip.com/2/1bij.jpg'
    return url
