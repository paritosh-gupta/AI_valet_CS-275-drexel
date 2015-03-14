import webapp2
import jinja2
import os
from EntityDatabaseManager import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Add(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('View/Add.html')
        self.response.write(template.render())
    def post(self):
        if(len(self.request.get("query"))!=0):
            print "value = " + str(len(self.request.get("query")))
            databaseHandler=Database()
            databaseHandler.search()
        else:
            name = self.request.get("name")
            command =self.request.get("command")
            description =self.request.get("description")
            databaseHandler = Database()
            databaseHandler.insert(name,command,description)


application = webapp2.WSGIApplication([
    ('/Add', Add),
    ], debug=True)
