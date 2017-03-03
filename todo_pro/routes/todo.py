from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect, header_with_headers, templates


def tdo(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    tds = ToDo.find_all(uid=u.id)
    s = ''
    for td in tds:
        ed = '<a href="/todo/edit?id={}">编辑</a>'.format(td.id)
        de = '<a href="/todo/delete?id={}">删除</a>'.format(td.id)
        s += '<h3>{}: {}    {}  {}</h3><br>'.format(td.id, td.title, ed, de)
    header = header_with_headers()
    body = templates('todo.html')
    body = body.replace('{{todos}}', s)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    if request.method == 'POST':
        form = request.form()
        td = ToDo.new(form)
        td.uid = u.id
        td.save()
    return redirect('/todo')


def delete(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    # TODO  id 为字符串时的处理
    i = int(request.query.get('id', -10))
    td = ToDo.find_by(id=i)
    if td is None or td.uid != u.id:
        return redirect('/todo')
    td.remove()
    return redirect('/todo')


def edit(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    # TODO 处理id不为数字的情况
    i = int(request.query.get('id', -10))
    td = ToDo.find_by(id=i)
    if td is None or td.uid != u.id:
        return redirect('/todo')
    header = header_with_headers()
    body = templates('edit.html')
    body = body.replace('{{id}}', str(td.id))
    body = body.replace('{{title}}', str(td.title))
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def update(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    if request.method == 'POST':
        form = request.form()
        # TODO 处理id 不为数字的情况
        i = int(form.get('id', -10))
        td = ToDo.find_by(id=i)
        if td is None or td.uid != u.id:
            return redirect('/todo')
        td.title = form.get('title', td.title)
        td.save()
    return redirect('/todo')


route_todo = {
    '/todo': tdo,
    '/todo/add': add,
    '/todo/edit': edit,
    '/todo/update': update,
    '/todo/delete': delete,
}
