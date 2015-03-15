__author__ = 'paritosh'

import webapp2
import jinja2
import os
from EntityDatabaseManager import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Process(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('View/Add.html')
        self.response.write(template.render())
    def post(self):
        databaseHandler= Database()
        speechText = self.request.get("json")
        words=speechText.split(" ")
        for word in words:
            entry=databaseHandler.search(word)
            if (entry)!="NULL":
                if(entry.action[0]!="/"):
                    if(entry.action[0-3]!="http"):
                        self.redirect("http://"+str(entry.action))
                else:
                    self.redirect(entry.action)
            else:
                print "word not found" + word

application = webapp2.WSGIApplication([
    ('/Process', Process),
    ], debug=True)

