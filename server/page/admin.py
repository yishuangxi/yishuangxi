#coding=utf-8
__author__ = 'db'
from common import base
import tornado.web
class AdminPage(base.BaseRequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("admin/admin.html")

class LoginPage(base.BaseRequestHandler):
    def get(self):
        self.render("admin/login.html")
    
    @base.db_closed
    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        
        db = self.get_db()
        try:
            user = db.get("select * from users where username=%s and password=%s", username, password)
            if user is not None:
                self.set_secure_cookie("username", username)
                self.redirect("/admin")
            else:
                self.write("登录失败")
        except:
            self.write("数据库错误")
class PublishPage(base.BaseRequestHandler):
    @tornado.web.authenticated
    @base.db_closed
    def get(self):
        db = self.get_db()
        cates = db.query("select * from cates order by create_time desc")
        self.render("admin/publish.html", cates=cates)
        
    @tornado.web.authenticated
    @base.db_closed
    def post(self):
        title = self.get_argument("title")
        ref_cate = self.get_argument("cate")
        content = self.get_argument("content")
        draft = int(self.get_argument("draft", 0))
        db = self.get_db()
        try:
            db.insert("insert into blogs values (null, %s, %s, %s, %s, null, null)",title, ref_cate, content,draft)
            print "draft", draft 
            if draft == 1:
                self.write("保存成功")
            else:
                self.write("发表成功")
        except:
            self.write("数据库错误")

class CateHandler(base.BaseRequestHandler):
    @tornado.web.authenticated
    @base.db_closed
    def post(self):
        name = self.get_argument("name")
        db = self.get_db()
        
        try:
            cate_id = db.insert("insert into cates values(null, %s, null)", name)
            self.write({
                "success":True,
                "data":{
                    "id":cate_id,
                    "name":name
                }
            })
        except:
            self.write({
                "success":False,
                "msg":"数据库错误"
            })
            
class ManageCates(base.BaseRequestHandler):
    @tornado.web.authenticated
    @base.db_closed
    def get(self):
        self.render("admin/manage_cates.html")
    
    @tornado.web.authenticated
    @base.db_closed
    def delete(self):
        cate_id = self.get_argument("cate")
        db = self.get_db()
        try:
            db.excute("delete from cates where id=%s", cate_id)
            self.write("删除成功！")
        except:
            self.write("数据库错误，删除失败！")