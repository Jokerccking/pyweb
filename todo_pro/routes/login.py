from Models.user import User
from routes import current_user, random_str, session, templates, header_with_headers


def route_login(request):
    method = request.method
    un = current_user(request)
    headers = {'Content-Type': 'text/html', }
    result = ''
    if method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_login() is True:
            un = u.username
            si = random_str()
            session[si] = {'username': u.username}
            headers['Set-Cookie'] = 'user={}'.format(si)
            result = '登录成功，欢迎你：{}'.format(u.username)
        else:
            un = u.username
            result = '用户名或密码错误！'
    header = header_with_headers(headers)
    body = templates('login.html')
    body = body.replace('{{result}}', result)
    body = body.replace('{{username}}', un)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
