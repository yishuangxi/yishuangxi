from page import index, admin

HANDLERS = [
    (r'/',index.IndexPage),
    (r'/pages/latest',index.LatestPage),
    (r'/pages/hotest',index.HotestPage),
    (r'/blogs/(\d+)', index.DetailPage),
    (r'/cates/(\d+)', index.CatePage),
    
    (r'/admin', admin.AdminPage),
    (r'/publish', admin.PublishPage),
    (r'/login', admin.LoginPage),
    (r'/cate', admin.CateHandler),
    (r'/manage_cates',admin.ManageCates)
]