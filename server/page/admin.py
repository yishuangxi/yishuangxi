__author__ = 'db'
from common import base


class AdminPage(base.BaseRequestHandler):
    def get(self):
        self.render("index.html")