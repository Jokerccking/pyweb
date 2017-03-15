from routes import json_response
from routes import current
from routes import redirect
from utils import log
from models.todo import Todo


def td_api_all(request):
    u = current(request)
    if u is None:
        return redirect('/login')
    tds = u.todos()
    ms = []
    for td in tds:
        t = td.to_dict()
        ms.append(t)
    return json_response(ms)


def td_api_add(request):
    u = current(request)
    form = request.json_form()
    if u is None or form.get('uid') is None:
        return redirect('/todo')
    td = Todo.new(form)
    return json_response(td.to_dict())


def td_api_delete(request):
    u = current(request)
    tdid = request.json_form().get('id')
    if u is None or tdid is None:
        return redirect('/todo')
    td = Todo.pop(int(tdid))
    return json_response(td.to_dict())


def td_api_update(request):
    u = current(request)
    form = request.json_form()
    tdid = form.get('tid')
    if u is None or tdid is None:
        return redirect('/todo')
    td = Todo.find(int(tdid))
    utd = td.update(form.get('content'))
    return json_response(utd.to_dict())

route_todo_api = {
    '/todo/api/all': td_api_all,
    '/todo/api/add': td_api_add,
    '/todo/api/delete': td_api_delete,
    '/todo/api/update': td_api_update,
}
