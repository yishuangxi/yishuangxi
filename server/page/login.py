__author__ = 'db'
from common import base


class LoginPage(base.BaseRequestHandler):
    def get(self):
        self.render("index.html")