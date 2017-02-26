from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect


def delete(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    i = int(request.query.get('id'))
    td = ToDo.find_by(id=i)
    if td is None or td.uid == u.id:
        return redirect('/todo')
    td.remove()
    return redirect('/todo')
