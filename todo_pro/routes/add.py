from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect


def add(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    if request.method == 'POST':
        form = request.form()
        td = ToDo.new(form)
        td.uid = u.id
        td.save()
    return redirect('/todo')