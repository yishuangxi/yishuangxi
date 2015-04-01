#coding=utf-8
import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SETTINGS = {
    "template_path": os.path.join(BASE_DIR, "web", "templates"),
    "static_path": os.path.join(BASE_DIR, "web", "static"),
    "debug": True,
    "cookie_secret": "EOFsnUQ/SeG2V39seKNw0hwYJSevqEjxs/+lMFfHSd4="
}