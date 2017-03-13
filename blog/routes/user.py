from utils import log
from routes import template
from routes import html_response
from models.user import User
from routes import current
from routes import (
    session,
    sid,
)

def index(request):
    um='YK'
    u = current(request)
    if u is not None:
        um = u.username
    body = template('index.html',um=um)
    return html_response(body)


def login(request):
    header = 'HTTP/1.1 200 OK\r\n'
    body = template('login.html')
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        uid = u.validate_login()
        if uid is not None:
            sesid = sid()
            session[sesid] = uid
            header = 'HTTP/1.1 200 OK\r\nSet-Cookie: user={}\r\n'.format(sesid)
            body = template('login.html',result='{}, Successfully Login!'.format(u.username))
        else:
            body = template('login.html',result='Name or Password is uncorrect!')+'\r\n'
    r = header +'\r\n'+body
    return r.encode(encoding='utf-8')



def register(request):
    result = ''
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        u = u.validate_register()
        result = 'Username has been token!'
        if u is not None:
            result='{},Successfully Regist!'.format(u.username)
    body = template('register.html',result=result)
    return html_response(body)





route_user = {
    '/': index,
    '/login': login,
    '/register': register,
}
