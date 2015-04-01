import tornado.web
import tornado.ioloop
from common import settings
from common import handlers


app = tornado.web.Application(handlers=handlers.HANDLERS, **settings.SETTINGS)

if __name__ == "__main__":
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()