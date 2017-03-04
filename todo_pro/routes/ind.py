from Models.user import User
from routes import template, random_str, session, header_with_headers, redirect, current_user


def index(request):
    un = '[游客]'
    u = current_user(request)
    if u is not None:
        un = u.username
    header = header_with_headers()
    body = template('index.html', um=un)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def login(request):
    rlt = ''
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_login() is True:
            si = random_str()
            session[si] = {'username': u.username}
            headers = {'Set-Cookie': 'user={}'.format(si)}
            return redirect('/', headers)
        else:
            rlt = '用户名或密码错误，请重新输入！'
    header = header_with_headers()
    body = template('login.html', result=rlt)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def register(request):
    rlt = ''
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_register():
            u.role = 10
            u.save()
            rlt = '注册成功！'
        else:
            rlt = '用户名和密码都必须大于两个字符！'

    header = header_with_headers()
    body = template('register.html', result=rlt)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


route_basic = {
    # static
    '/': index,
    '/login': login,
    '/register': register,
}
