from Models.user import User
from routes import current_user, templates, random_str, session, header_with_headers, redirect


def index(request):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    username = current_user(request)
    body = templates('index.html')
    body = body.replace('{{um}}', username)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def login(request):
    method = request.method
    un = current_user(request)
    headers = {'Content-Type': 'text/html', }
    result = ''
    if method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_login() is True:
            # un = u.username
            si = random_str()
            session[si] = {'username': u.username}
            headers['Set-Cookie'] = 'user={}'.format(si)
            # result = '登录成功，欢迎你：{}'.format(u.username)
            return redirect('/todo', headers)
        else:
            un = u.username
            result = '用户名或密码错误！'
    header = header_with_headers(headers)
    body = templates('login.html')
    body = body.replace('{{result}}', result)
    body = body.replace('{{username}}', un)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def register(request):
    method = request.method
    result = ''
    if method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_register() is True:
            u.save()
            result = '注册成功！<br><prep>{}</prep>'.format(User.all())
        else:
            result = '用户名和密码都必须大于两个字符！'

    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = templates('register.html')
    body = body.replace('{{result}}', result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


route_basic = {
    # static
    '/': index,
    '/login': login,
    '/register': register,
}
