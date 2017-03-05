from Models import Model
from Models.user import User


class Comment(Model):
    def __init__(self, form):
        self.id = int(form.get('id', -1))
        self.mbid = int(form.get('mbid', -1))
        self.uid = int(form.get('uid', -1))
        self.content = form.get('content', '')

    def user(self):
        return User.find_by(id=self.uid)