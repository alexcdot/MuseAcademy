#!/usr/bin/env python

import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(BaseHandler):
    def get(self):
        self.render('content.html')

class Data(BaseHandler):
    def get(self):
        self.redirect('/')

    def post(self):
        gamma = self.request.get('gamma')
        params = dict(gamma=gamma)
        self.render('param.html', **params)

class CalmState(BaseHandler):
    def post(self):
        calm_state = self.request.get('calm_state')
        params = dict(calm_state=calm_state)
        self.render('param.html', **params)

class StressState(BaseHandler):
    def post(self):
        stress_state = self.request.get('stress_state')
        params = dict(stress_state=stress_state)
        self.render('param.html', **params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/bw_index', Data),
    ('/calm_state', CalmState),
    ('/stress_state', StressState)
], debug=True)
