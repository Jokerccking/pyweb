import socket
import urllib.parse
import _thread
import json

from routes.user import route_user
from routes.todo import route_todo
from routes.todo_api import route_todo_api
from routes.blog import route_blog
from routes.static import route_static
from utils import log

class Request(object):
    def __init__(self):
        self.method = ''
        self.path = ''
        self.query = {}
        self.headers = {}
        self.cookies = {}
        self.body = {}

    def form(self):
        f = {}
        li = self.body.split('&')
        for e in li:
            if '=' in e:
                k, v = e.split('=')
                key = urllib.parse.unquote(k)
                value = urllib.parse.unquote(v)
                f[key] = value
        return f

    def __repr__(self):
        return self.method + self.path

    def json_form(self):
        #log("req.body::",self.body)
        #log("jsonform::", json.loads(self.body))
        return json.loads(self.body)


def parse_path(path):
    query = {}
    if '?' in path:
        path, q = path.split('?',1)
        qs = q.split('&')
        for e in qs:
            k, v = e.split('=')
            query[k] = v
    return path, query


def parse_cookies(headers):
    cookies = {}
    cks = headers.get('Cookie')
    if cks is not None:
        cks = cks.split(';')
        for ck in cks:
            if '=' in ck:
                k, v = ck.split('=')
                cookies[k.strip()] = v.strip()
    return cookies


def parse_headers(rh):
    headers = {}
    li = rh.split('\r\n')
    for e in li:
        if ':' in e:
            k, v = e.split(':', 1)
            k, v = k.strip(), v.strip()
            headers[k] = v
    return headers


def parse_request(r):
    header, body = r.split('\r\n\r\n', 1)
    rl, rh = header.split('\r\n',1)
    method = rl.split()[0]
    p = rl.split()[1]
    path ,query = parse_path(p)
    headers = parse_headers(rh)
    cookies = parse_cookies(headers)
    return method, path, query, headers, cookies, body


# TODO ???
def error(request, code=404):
    log(request.path,'error::::::Not Found')
    d = {
        404: b'HTTP/1.1 404 NotFound\r\n\r\n',
    }
    return d.get(code,b'')


def response_for_request(request):
    path = request.path
    route = {
        '/static': route_static,
    }
    route.update(route_user)
    route.update(route_todo)
    route.update(route_todo_api)
    route.update(route_blog)
    response = route.get(path, error)
    return response(request)


def process(connection):
    req = connection.recv(1024).decode('utf-8')
    if (len(req.split())) < 4:
        connection.close()
    try:
        req.replace('\n','\r\n')
        #log('request change \r\n done')
    except Exception as e:
        log('request\r\nexception',e)

    r = Request()
    r.method, r.path, r.query, r.headers, r.cookies, r.body = parse_request(req)
    #log('original request::',req)
    log('path::::::',r.path)

    resp = response_for_request(r)
    connection.sendall(resp)
    #try:
    #    resp.decode('utf-8').replace('\r\n','\n')
    #except Exception as e:
    #    log('Exception::::', e)

    connection.close()

def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host,port))
        s.listen(5)
        log('port server listened:::', port)
        while True:
            connection, address = s.accept()
            _thread.start_new_thread(process,(connection,))


if __name__ == '__main__':
    config = dict(
        host='',
        port=3000,
    )
    run(**config)

