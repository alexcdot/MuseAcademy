#!/usr/bin/env python

import webapp2
import jinja2
import os
from google.appengine.ext import db
from numpy.distutils.fcompiler import none

def brain_waves(name='default'):
    return db.Key.from_path('users', name)

class BrainWaves(db.Model):
    calm_state_avg = db.FloatProperty(required=True)
    stress_state_avg = db.FloatProperty(required=True)
    list_gamma_values = db.ListProperty(item_type=float, required=True)

CONST_points = 300
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

calm_state = 0
stress_state = 0
is_account_created = False
lst = []

def createAcct(self):
    new_acct = BrainWaves(parent=brain_waves_key(), calm_state=calm_state, stress_state=stress_state)
    new_acct.put()
    for i in range(CONST_points):
        lst[i] = 0      


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
        lst.append(data_point)
        start_index = len(lst) - CONST_points
        end_index = len(lst) - 1
        
        end_time = len(list) / 60.0 # how many times 60 iterations have passed
        start_time = end_time - 5
        # incrValue = 1 / 300.0
        tVals = numpy.linspace(start_time, endTime, ) 
        
        params = dict(list = lst[start_index:end_index], start_time=start_time, end_time=end_time, incrValue=incrValue)
        self.render('graph.html', **params)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/calm_state', CalmState),
    ('/stress_state', StressState),
    ('/gamma_value', GammaWaveValue)
], debug=True)
