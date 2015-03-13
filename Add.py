import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Add(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('View/Add.html')
        self.response.write(template.render())
    # def post(self):
    #     email = self.request.get("name")
    #     if(email=="paritosh"):



application = webapp2.WSGIApplication([
    ('/Add', Add),
    ], debug=True)
