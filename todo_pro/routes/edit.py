from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect, header_with_headers, templates


def edit(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    i = int(request.query.get('id'))
    td = ToDo.find_by(id=i)
    if td is None or td.uid != u.id:
        return redirect('/todo')
    header = header_with_headers({})
    body = templates('edit.html')
    body = body.replace('{{id}}', td.id)
    body = body.replace('{{title}}', td.title)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
