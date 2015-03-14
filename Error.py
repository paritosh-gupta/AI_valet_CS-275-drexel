import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Error(webapp2.RequestHandler):

    def get(self):
	  template = JINJA_ENVIRONMENT.get_template('View/error.html')
	  self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', Error),
], debug=True)
__author__ = 'paritosh'
