#coding=utf-8
import tornado.web
import torndb
import settings
class BaseRequestHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")
    def get_db(self):
        return torndb.Connection(settings.mysql_server, settings.mysql_db, user=settings.user)
    
    def get_user(self):
        db = self.get_db()
        user = db.get("select * from users where username=%s", self.get_secure_cookie("username"))
        return user
        
    def get_cates_view(self):
        db = self.get_db()
        cates = db.query("select * from cates_view")
        return cates
        
    def narrow_blogs(self, blogs):
        for blog in blogs:
            blog['content'] = blog['content'][0:50]+ '...'


def db_closed(fn):
    def inner(self, *args, **kwargs):
        fn(self, *args, **kwargs)
        try:
            self.db.close()
        except:
            self.write("数据库关闭出错！")
    return inner
        
    
