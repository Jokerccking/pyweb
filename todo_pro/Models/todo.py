from Models import Model


class ToDo(Model):
    def __init__(self, form):
        self.id = int(form.get('id', -1))
        self.uid = int(form.get('uid', -1))
        self.title = form.get('title', '')
