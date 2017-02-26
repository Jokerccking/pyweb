from Models.message import Message
from routes import current_user, templates, redirect


def route_message(request):
    username = current_user(request)
    msg = ''
    if username == '[游客]':
        return redirect('/')
    if request.method == 'POST':
        form = request.form
        m = Message.new(form)
        m.save()
        msg = '<br>'.join([str(m) for m in Message.all()]) + '你好：{}'.format(username)

    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = templates('html_basic.html')
    body = body.replace('{{messages}}', msg)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
