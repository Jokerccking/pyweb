from Models.todo import ToDo
from routes import redirect, header_with_headers, template, current_user, login_required
from utils import current_time


def tdo(request):
    u = current_user(request)
    ts = ToDo.find_all(uid=u.id)
    header = header_with_headers()
    body = template('todo.html', tds=ts)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    u = current_user(request)
    # TODO 如果请求的title是空的呢？
    # TODO 输入的空格显示为了‘+’号
    if request.method == 'POST':
        form = request.form()
        td = ToDo.new(form)
        td.uid = u.id
        td.created_time = current_time()
        td.save()
    return redirect('/todo')


def delete(request):
    u = current_user(request)
    # TODO  id 为字符串时的处理
    i = int(request.query.get('id', -10))
    td = ToDo.find_by(id=i)
    if td is None or td.uid != u.id:
        return redirect('/todo')
    td.remove()
    return redirect('/todo')


def edit(request):
    u = current_user(request)
    # TODO 处理id不为数字的情况
    i = int(request.query.get('id', -10))
    td = ToDo.find_by(id=i)
    if td is None or td.uid != u.id:
        return redirect('/todo')
    header = header_with_headers()
    # TODO str(td.id)????
    body = template('edit.html', id=td.id, title=td.title)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def update(request):
    u = current_user(request)
    if request.method == 'POST':
        form = request.form()
        # TODO 处理id 不为数字的情况
        i = int(form.get('id', -10))
        td = ToDo.find_by(id=i)
        if td is None or td.uid != u.id:
            return redirect('/todo')
        td.title = form.get('title', td.title)
        td.update_time = current_time()
        td.save()
    return redirect('/todo')


route_todo = {
    '/todo': login_required(tdo),
    '/todo/add': login_required(add),
    '/todo/edit': login_required(edit),
    '/todo/update': login_required(update),
    '/todo/delete': login_required(delete),
}
