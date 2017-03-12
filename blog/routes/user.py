from routes import template
from routes import html_response
from models.user import User
from routes import (
    session,
    sid,
)

def index(request):

    body = template('index.html')
    return html_response(body)


def login(request):
    r = template('login.html')+'\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        uid = u.validate_login()
        if i is not None:
            sid = sid()
            session[sid] = uid
            header = 'HTTP/1.1 200 OK\r\nSet-Cookie: user={}\r\n'.format(sid)
            body = template('login.html',result='Hello {}!'.format(u.username))
            r = header +'\r\n' + body
        else:
            r = template('index.html',result='Name or Password is uncorrect!')+'\r\n'
    return r.encode(encoding='utf-8')


def register(request):
    result = ''
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        u = u.validate_register()
        result='Successfully Registe!'
        if u is None:
            result = 'Username has been token!'
    body = template('register.html',result=result)
    return html_response(body)





route_user = {
    '/': index,
    '/login': login,
    '/register': register,
}
