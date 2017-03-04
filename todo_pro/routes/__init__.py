from os.path import dirname
import random

from jinja2 import Environment
from jinja2 import FileSystemLoader

from Models.user import User

session = {
    'session_id': {
        'username': 'name'
    }
}

path = '{}/templates/'.format(dirname(dirname(__file__)))
env = Environment(loader=FileSystemLoader(path))


def template(mod, **kwargs):
    t = env.get_template(mod)
    return t.render(**kwargs)


def redirect(p, headers=None):
    r = 'HTTP/1.1 302 Moved Temporatily\r\nLocation: {}\r\n'.format(p)
    # TODO 判定headers为字典
    if headers is not None:
        for k, v in headers.items():
            r += '{}: {}\r\n'.format(k, v)
    r += '\r\n'
    return r.encode(encoding='utf-8')


def current_user(request):
    session_id = request.cookies.get('user', '')
    un = session.get(session_id, {}).get('username', '[游客]')
    u = User.find_by(username=un)
    return u


def login_required(routes):
    def func(request):
        if current_user(request) is None:
            return redirect('/login')
        return routes(request)
    return func


def random_str():
    seed = 'as2df3ei5nfl6kd2309jhd5i7fh782ttb9jhe8dfr51d210f5we1fd0cfv'
    s = ''
    for i in range(15):
        v = random.randint(0, len(seed) - 1)
        s += seed[v]
    return s


def header_with_headers(headers=None):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    hs = ''
    if headers is not None:
        for k, v in headers.items():
            hs += '{}:{}\r\n'.format(k, v)
    return header + hs


# def test_tmp():
#     return template('login.html', um='roy')
#
# if __name__ == '__main__':
#     log('path:::::::::', test_tmp())
