#coding=utf-8
__author__ = 'db'
from common import base
import tornado.web
class AdminPage(base.BaseRequestHandler):
    @tornado.web.authenticated
    def get(self):
        db = self.get_db()
        cates = db.query("select * from cates")
        self.render("admin/admin.html", cates=cates)

class LoginPage(base.BaseRequestHandler):
    def get(self):
        self.render("admin/login.html")
    
    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        
        print username
        print password
        db = self.get_db()
        try:
            user = db.get("select * from users where username=%s and password=%s", username, password)
            if user is not None:
                self.set_secure_cookie("username", username)
                self.redirect("/admin")
        except:
            self.write("登录失败")
        
class PublishHandler(base.BaseRequestHandler):
    @tornado.web.authenticated
    def post(self):
        title = self.get_argument("title")
        ref_cate = self.get_argument("cate")
        content = self.get_argument("content")
        
        db = self.get_db()
        try:
            db.insert("insert into blogs values (null, %s, %s, %s, null, null)",title, ref_cate, content)
            self.write("发表成功")
        except:
            self.write("数据库错误")