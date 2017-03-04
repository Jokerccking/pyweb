import random

from Models.user import User

session = {
    'session_id': {
        'username': 'name'
    }
}


def redirect(path, headers=None):
    r = 'HTTP/1.1 302 Moved Temporatily\r\nLocation: {}\r\n'.format(path)
    if headers is not None:
        for k, v in headers.items():
            r += '{}: {}\r\n'.format(k, v)
    r += '\r\n'
    return r.encode(encoding='utf-8')


def current_user(request):
    session_id = request.cookies.get('user', '')
    username = session.get(session_id, {}).get('username', '[游客]')
    return username


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


def validate_routes(route):
    """
    给函数增加代码
    :param route:
    :return:
    """
    def f(request):
        um = current_user(request)
        u = User.find_by(username=um)
        if u is None:
            redirect('/')
        return route(request)

    return f
