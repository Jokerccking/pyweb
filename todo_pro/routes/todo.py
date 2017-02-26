from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect, header_with_headers, templates


def to_do(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    tds = ToDo.find_all(id=u.id)
    s = ''
    for td in tds:
        ed = '<a href="/todo/edit?id={}">编辑</a>'.format(td.id)
        de = '<a href="/todo/delete?id={}">删除</a>'.format(td.id)
        s += '<h3>{}: {}    {}  {}</h3><br>'.format(td.id, td.title, ed, de)
    header = header_with_headers({})
    body = templates('todo.html')
    body = body.replace('{{todos}}', s)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
