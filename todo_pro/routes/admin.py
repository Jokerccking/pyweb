from Models.user import User
from routes import current_user, redirect, header_with_headers, template


def admin_users(request):
    u = current_user(request)
    if u is None or u.role != 1:
        return redirect('/')
    us = User.all()
    header = header_with_headers()
    body = template('admin_users.html', users=us)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def pwd_reset(request):
    u = current_user(request)
    if u is None or u.role != 1:
        return redirect('/')
    form = request.form()
    # TODO 处理id不为数字的情况
    usr = User.find_by(id=int(form.get('id', -10)))
    if usr is not None:
        usr.password = form.get('password', '')
        usr.save()
    return redirect('/admin/users')


route_admin = {
    '/admin/users': admin_users,
    '/admin/user/update': pwd_reset
}
