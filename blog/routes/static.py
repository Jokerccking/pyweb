from utils import log

def route_static(request):
    filename = request.query.get('file')
    # TODO ?? relative path??
    path = 'statics/' + filename
    body = b''
    with open(path, 'rb') as f:
        body += f.read()
    header = b'HTTP/1.1 200 OK\r\n'
    r = header + b'\r\n' + body
    return r
