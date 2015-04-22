__author__ = 'db'

from common import base

class PublishPage(base.BaseRequestHandler):
    def get(self):
        self.render("publish.html")