from utils import log
from routes import current
from routes import json_response
from routes import redirect
from models.blog import Blog
from models.blog import Comment


def b_api_all(request):
    u = current(request)
    if u is None:
        return redirect('/login')
    bs = u.blogs()
    ms = []
    for b in bs:
        ms.append(b.to_dict())
    return json_response(ms)


def b_api_add(request):
    u = current(request)
    form = request.json_form()
    uid = form.get('uid')
    if u is None or uid is None:
        return redirect('/blog')
    b = Blog.new(form)
    return json_response(b.to_dict())


def b_api_delete(request):
    u = current(request)
    bid = request.query.get('id')
    if u is None or bid is None:
        return redirect('/blog')
    b = Blog.popi(int(bid))
    return json_response(b.to_dict())

def b_api_cmtadd(request):
    u = current(request)
    form = request.json_form()
    bid = form.get('bid')
    if u is None or bid is None:
        return redirect('/blog')
    form['um'] = u.username
    cmt = Comment.new(form)
    return json_response(cmt.to_dict())

def b_api_cmtdelete(request):
    u = current(request)
    cid = request.query.get("id")
    if u is None or cid is None:
        return redirect('/blog')
    cmt = Comment.pop(int(cid))
    return json_response(cmt.to_dict())


route_blog_api = {
    '/blog/api/all': b_api_all,
    '/blog/api/add': b_api_add,
    '/blog/api/delete': b_api_delete,
    '/blog/api/cmt_add': b_api_cmtadd,
    '/blog/api/cmt_delete': b_api_cmtdelete,
}
