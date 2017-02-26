import socket
import urllib.parse

from routes import route_dict
from utils import log


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


def parse_path(path):
    query = {}
    if '?' in path:
        path, q = path.split('?')
        qs = q.split('&')
        for e in qs:
            k, v = e.split('=')
            query[k] = v
    return path, query


def parse_cookies(headers):
    cookies = {}
    cks = headers.get('Cookie')
    if cks is not None:
        cks = cks.split('; ')
        for ck in cks:
            k, v = ck.split('=')
            cookies[k] = v
    return cookies


def parse_headers(rh):
    headers = {}
    li = rh.split('\r\n')
    for e in li:
        k, v = e.split(':', 1)
        headers[k] = v
    return headers


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


def error(request, code=404):
    log('请求错误，找不到资源：：：', request)
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Not Found</h1>'
    }
    return e.get(code, b'')


def response_for_request(request):
    path = request.path
    response = route_dict.get(path, error)
    return response(request)


def run(host='', port=3000):
    r = Request()
    with socket.socket() as s:
        s.bind((host, port))
        log('服务器监听端口：', port)
        while True:
            s.listen(5)
            connection, address = s.accept()
            log('请求来自ip：', address)

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
