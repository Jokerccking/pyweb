def static(request):
    filename = request.query.get('file','doge.gif')
    # TODO ?? relative path??
    path = 'static/' + filename
    body = b''
    with open(path, 'rb') as f:
        body += f.read
    header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n'
    r = header + '\r\n\r\n' + body
    return r
