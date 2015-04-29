from common import base


class IndexPage(base.BaseRequestHandler):
    @base.db_closed
    def get(self):
        db = self.get_db()
        cates = self.get_cates_view()
        self.render("index.html", cates=cates)


class LatestPage(base.BaseRequestHandler):
    @base.db_closed
    def get(self):
        db = self.get_db()
        blogs = db.query('select * from blogs_view order by pub_time desc limit 10')
        self.narrow_blogs(blogs)
        self.render('pages/latest.html', blogs=blogs)         
        
class HotestPage(base.BaseRequestHandler):
    @base.db_closed
    def get(self):
        db = self.get_db()
        blogs = db.query('select * from blogs_view order by comment_counts desc limit 10')
        self.render('pages/hotest.html', blogs=blogs)
      
        
class CatePage(base.BaseRequestHandler):
    @base.db_closed
    def get(self, cate_id):
        db = self.get_db()
        blogs = db.query("select * from blogs_view where ref_cate=%s order by pub_time desc", cate_id)
        curr_cate = db.get("select * from cates where id=%s", cate_id)
        self.render("pages/cate.html", blogs=blogs, curr_cate=curr_cate)
        
        
class DetailPage(base.BaseRequestHandler):
    @base.db_closed
    def get(self, blog_id):
        db = self.get_db()
        blog = db.get('select * from blogs where id=%s', blog_id)
        self.render('pages/detail.html', blog=blog)


        