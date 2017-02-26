from Models import Model


class ToDo(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        if self.id is not None:
            self.id = int(self.id)
        self.uid = form.get('uid', None)
        if self.uid is not None:
            self.uid = int(self.uid)
        self.title = form.get('title', '')
