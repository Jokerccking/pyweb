import socket
import urllib.parse

from routes.admin import route_admin
from routes.ind import route_basic
from routes.microb import route_microb
from routes.static import route_static
from routes.todo import route_todo
from utils import log, parse_path, parse_headers, parse_cookies, error


class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.headers = {}
        self.cookies = {}
        self.body = ''

    def form(self):
        f = {}
        li = self.body.split('&')
        for e in li:
            k, v = e.split('=')
            key = urllib.parse.unquote(k)
            value = urllib.parse.unquote(v)
            f[key] = value
        return f

    def __repr__(self):
        return self.method + self.path


def parse_request(r):
    # method, path, query, headers, cookies, body = '', '', {}, {}, {}, ''
    header, body = r.split('\r\n\r\n')
    rl, rh = header.split('\r\n', 1)
    method = rl.split()[0]
    p = rl.split()[1]
    path, query = parse_path(p)
    headers = parse_headers(rh)
    cookies = parse_cookies(headers)
    return method, path, query, headers, cookies, body


def response_for_request(request):
    path = request.path
    route = {
        '/static': route_static,
    }
    route.update(route_basic)
    route.update(route_todo)
    route.update(route_admin)
    route.update(route_microb)
    response = route.get(path, error)
    return response(request)


def run(host='', port=3000):
    r = Request()
    with socket.socket() as s:
        s.bind((host, port))
        log('服务器监听端口：', port)
        while True:
            s.listen(5)
            connection, address = s.accept()

            req = connection.recv(1024)
            req = req.decode('utf-8')
            if len(req.split()) < 2:
                continue
            r.method, r.path, r.query, r.headers, r.cookies, r.body = '', '', {}, {}, {}, ''
            r.method, r.path, r.query, r.headers, r.cookies, r.body = parse_request(req)

            resp = response_for_request(r)
            connection.sendall(resp)

            connection.close()


if __name__ == '__main__':
    config = dict(
        host='',
        port=3000,
    )
    run(**config)
