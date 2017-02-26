def route_static(request):
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    body = b''
    with open(path, 'rb') as f:
        body += f.read()
    header = b'HTTP/1.1 200 OK\r\n'
    r = header + b'' + body
    return r
