from Models.comment import Comment
from Models.mcrioblog import Microblog
from Models.user import User
from routes import current_user, header_with_headers, template, login_required, redirect


def micb(request):
    u = current_user(request)
    us = User.exp(id=u.id)
    gid = request.query.get('uid')
    # TODO uid为非数字
    if gid is None or gid == str(u.id):
        mh = u
        un = 'My'
        mbs = Microblog.find_all(uid=u.id)
        delete = '删除'
    else:
        uid = int(gid)
        mh = User.find_by(id=uid)
        mbs = Microblog.find_all(uid=uid)
        g = User.find_by(id=uid)
        un = "{}'s".format(g.username)
        delete = ''

    header = header_with_headers()
    body = template('microb.html', mh=mh, ur=u.username, un=un, mbs=mbs, us=us, delete=delete, uid=u.id)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def mb_cmt(request):
    u = current_user(request)
    form = request.form()
    uid = int(form.get('uid', -10))
    mid = int(form.get('mbid', -10))
    mb = Microblog.find_by(id=mid)
    cur = User.find_by(id=uid)
    if mb is None or cur is None or cur.id != u.id:
        return redirect('/microb')
    cm = Comment.new(form)
    cm.save()
    return redirect('/microb?uid={}'.format(mb.uid))


def mb_add(request):
    u = current_user(request)
    mb = Microblog.new(request.form())
    mb.uid = u.id
    mb.save()
    return redirect('/microb')


def mb_mbdel(request):
    u = current_user(request)
    # TODO
    i = int(request.query.get('mid', -10))
    mb = Microblog.find_by(id=i)
    if mb is None or mb.uid != u.id:
        return redirect('/microb')
    mb.remove()
    for cm in mb.comments():
        cm.remove()
    return redirect('/microb')


def mb_cmtdel(request):
    u = current_user(request)
    i = int(request.query.get('cid', -10))
    cm = Comment.find_by(id=i)
    if cm is None:
        return redirect('/microb')
    mb = Microblog.find_by(id=cm.mbid)
    cur = cm.user()
    ur = mb.user()
    if u.id == cur.id or u.id == ur.id:
        cm.remove()
    return redirect('/microb?uid={}'.format(mb.uid))


route_microb = {
    '/microb': login_required(micb),
    '/microb/add': login_required(mb_add),
    '/microb/delete': login_required(mb_mbdel),
    '/microb/comment': login_required(mb_cmt),
    '/microb/cmtdel': login_required(mb_cmtdel)
}
