import random

from Models.user import User

session = {
    'session_id': {
        'username': 'name'
    }
}


def redirect(path, headers=None):
    r = 'HTTP/1.1 302 Moved Temporatily\r\nLocation: {}\r\n'.format(path)
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


def templates(name):
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    return s


def random_str():
    seed = 'asdfeinflkd2309jhdifh782ttbjhedfr51d210f5we1fd0cfv'
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
