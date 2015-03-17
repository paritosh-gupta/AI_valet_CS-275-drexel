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
        self.redirect("/")
    def post(self):
        databaseHandler= Database()
        speechText = self.request.get("json")
        words=speechText.split(" ")
        for word in words:
            entry=databaseHandler.search(word)
            if (entry)!="NULL":
                print "url=" + entry.action
                if(entry.action[0]!="/"):
                    if(entry.action[0-3]!="http"):
                        self.redirect("http://"+str(entry.action))
                    else:
                        self.redirect(str(entry.action))
                else:
                    self.redirect(entry.action)
            else:
                print "word not found " + word

application = webapp2.WSGIApplication([
    ('/Process', Process),
    ], debug=True)

