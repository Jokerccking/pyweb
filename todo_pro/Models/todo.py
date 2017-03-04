from Models import Model


class ToDo(Model):
    def __init__(self, form):
        self.id = int(form.get('id', -1))
        self.uid = int(form.get('uid', -1))
        self.title = form.get('title', '')
        self.created_time = form.get('created_time', '')
        self.update_time = form.get('update_time', '')
