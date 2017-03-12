from routes import current
from routes import template
from routes import redirect

def todo(request):
    u = current(request)
    if u is None:
        return redirect('/')
    body = template('todo.html',um=u.username)
    return html_response(body)

route_todo = {
    '/todo': todo,
}
