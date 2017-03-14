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
    if u is None and form.get('uid') is None:
        return redirect('/login')
    td = Todo.new(form)
    return json_response(td.to_dict())


def td_api_delete(request):
    u = current(request)
    tid = request.json_form().get('id')
    log('td:::::id',tid)
    if u is None and tid is None:
        return redirect('/todo')
    td = Todo.pop(tid)
    return json_response(td.to_dict())


route_todo_api = {
    '/todo/api/all': td_api_all,
    '/todo/api/add': td_api_add,
    '/todo/api/delete': td_api_delete,
}
