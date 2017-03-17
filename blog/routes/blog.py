from routes import current
from routes import template
from routes import redirect
from routes import html_response
from models.user import User

def blog(request):
    u = current(request)
    if u is None:
        return redirect('/')
    users = u.others()
    body = template('blog.html',um=u.username,uid=u.id,users=users)
    return html_response(body)

def blog_view(request):
    u = current(request)
    hid = requeset.query.get('id')
    if u is None or hid is None:
        return redirect('/login')
    users = u.others()
    h = User.find(int(hid))
    body = template('view.html',um=u.username,hum=h.username,hid=h.id,users=users)
    return html_response(body)


route_blog = {
    '/blog': blog,
    '/blog/view': blog_view,
}
