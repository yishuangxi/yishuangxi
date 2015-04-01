from common import base


class IndexPage(base.BaseRequestHandler):
    def get(self):
        self.render("index.html")