from Models import Model
from Models.comment import Comment
from Models.user import User


class Microblog(Model):
    def __init__(self, form):
        self.id = int(form.get('id', -1))
        self.uid = int(form.get('uid', -1))
        self.blog = form.get('blog', '')

    def comments(self):
        return Comment.find_all(mbid=self.id)

    def user(self):
        return User.find_by(id=self.uid)