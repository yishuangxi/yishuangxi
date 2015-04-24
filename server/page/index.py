from common import base


class IndexPage(base.BaseRequestHandler):
    @base.db_closed
    def get(self):
        db = self.get_db()
        cates = self.get_cates_view()
        blogs_latest = db.query('select * from blogs order by pub_time asc limit 3')
        blogs_hottest = db.query('select * from blogs_view order by comment_counts desc limit 3')
        print "blogs_hottest", blogs_hottest
        self.render("index.html", cates=cates, blogs_latest=blogs_latest, blogs_hottest=blogs_hottest)