from routes import current
from routes import template
from routes import redirect
from routes import html_response

def todo(request):
    #log('session',session)
    u = current(request)
    #log('u:::',u)
    if u is None:
        return redirect('/login')
    body = template('todo.html',um=u.username)
    return html_response(body)

route_todo = {
    '/todo': todo,
}
