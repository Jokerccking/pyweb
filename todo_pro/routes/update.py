from Models.todo import ToDo
from Models.user import User
from routes import current_user, redirect


def update(request):
    um = current_user(request)
    u = User.find_by(username=um)
    if u is None:
        return redirect('/')
    if request.method == 'POST':
        form = request.form()
        i = int(form.get('id', -1))
        td = ToDo.find_by(id=i)
        if td is None or td.uid != u.id:
            return redirect('/todo')
        td.title = form.get('title', td.title)
        td.save()
    return redirect('/todo')
