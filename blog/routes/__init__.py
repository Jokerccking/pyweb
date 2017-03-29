import os.path
import json
from jinja2 import Environment, FileSystemLoader
import random
from models.user import User



session = {}

def sid():
    seed = 'feisw^778hufhebsdiuhikishfi'
    s = ''
    for i in range(16):
        s += seed[random.randint(0, len(seed)-1)]
    return s


def redirect(url):
    header = 'HTTP/1.1 302 Temporarily Moved\r\nContent-Type: text/html\r\nLocation: {}\r\n'.format(url)
    body = ''
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def html_response(body):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def json_response(body):
    header = 'HTTP/1.1 200 OK\r\nContect-Type: application/json\r\n'
    body = json.dumps(body,ensure_ascii=False)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def confirm(route):
    def f(request):
        form = request.form()
        u = current(request)
        if u.username != form.get('user'):
            return redirect('/')
        return route(request)


def current(request):
    sid = request.cookies.get('user','')
    uid = int(session.get(sid, -1))
    return User.find(uid)


# TODO code block?
path = 'templates'.format(os.path.dirname(__file__))
loader = FileSystemLoader(path)
env = Environment(loader=loader)


def template(path, **kwargs):
    t = env.get_template(path)
    return t.render(**kwargs)

