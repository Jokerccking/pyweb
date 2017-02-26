from routes import current_user, templates


def index(request):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    username = current_user(request)
    body = templates('index.html')
    body.replace('{{username}}', username)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
