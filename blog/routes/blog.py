from routes import current
from routes import current
from routes import template


def blog(request):
    u = current(request)
    if u is None:
        return redirect('/')
    body = template('blog.html')
    return html_response(body,um=u.username)

route_blog = {
    '/blog': blog,
}
