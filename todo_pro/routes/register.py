from Models.user import User
from routes import templates


def route_register(request):
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
