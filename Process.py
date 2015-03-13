__author__ = 'paritosh'

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Process(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('View/Add.html')
        self.response.write(template.render())
    def post(self):
        json = self.request.get("name")
        print json
        webapp2.redirect("/nope")



application = webapp2.WSGIApplication([
    ('/Process', Process),
    ], debug=True)

