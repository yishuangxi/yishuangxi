from page import index, admin, publish, login

HANDLERS = [
    (r'/',index.IndexPage),
    (r'/admin', admin.AdminPage),
    (r'/publish', publish.PublishPage),
    (r'/login', login.LoginPage)
]