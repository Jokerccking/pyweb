from routes import current
from routes import template
from routes import redirect
from routes import html_response

def blog(request):
    u = current(request)
    if u is None:
        return redirect('/')
    body = template('blog.html',um=u.username,uid=u.id)
    return html_response(body)

route_blog = {
    '/blog': blog,
}
