from google.appengine.ext import ndb

class Car(ndb.Model):
    type = ndb.StringProperty(required=True)
    year = ndb.StringProperty(required=True)
    color = ndb.StringProperty(required=True)

    def doSomething(self):
        print(self.type+ "hello there")
        return ""
car1 = Car(type = "Toyota", year = "2012", color = "gold")
print(car1.doSomething())
