#!/usr/bin/env python

import webapp2
import jinja2
import os
from google.appengine.ext import db

def brain_waves(name='default'):
    return db.Key.from_path('users', name)

class BrainWaves(db.Model):
    calm_state_avg = db.FloatProperty(required=True)
    stress_state_avg = db.FloatProperty(required=True)
    list_gamma_values = db.ListProperty(item_type=float, required=True)


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

calm_state = 0
stress_state = 0
is_account_created = False

def createAcct(self):
    new_acct = BrainWaves(parent=brain_waves_key(), calm_state=calm_state, stress_state=stress_state)
    new_acct.put()

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
        self.render('index.html')

class CalmState(BaseHandler):
    def post(self):
        calm_state = self.request.get('state')
        params = dict(calm_state=calm_state)
        self.render('param.html', **params)

        if (calm_state != 0 and stress_state != 0):
            createAcct()

class StressState(BaseHandler):
    def post(self):
        stress_state = self.request.get('state')
        params = dict(stress_state=stress_state)
        self.render('param.html', **params)

        if (calm_state != 0 and stress_state != 0):
            createAcct()

class GammaWaveValue(BaseHandler):
    def post(self):
        data_point = self.request.get('data_point')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/calm_state', CalmState),
    ('/stress_state', StressState)
], debug=True)
