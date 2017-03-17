from utils import log
from models import Model
from models.todo import Todo
from models.blog import Blog
from models.blog import Comment

class User(Model):
    @classmethod
    def find_all(cls):
        return cls.all()

    def __init__(self,form):
        self.id = form.get('id')
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.role = 10

    def salted_password(self, password, salt='$i3&f*k'):
        import hashlib
        hash1 = hashlib.sha256(password.encode('ascii')).hexdigest()
        hash2 = hashlib.sha256((hash1 + salt).encode('ascii')).hexdigest()
        return hash2

    def validate_login(self):
        b = None
        #self.password = self.salted_password(self.password)
        us = User.all()
        for u in us:
            if u.username == self.username and u.password == self.password:
                b = u.id
                break
        return b

    def validate_register(self):
        us = User.all()
        #self.password = self.salted_password(self.password)
        for u in us:
            if u.username == self.username:
                return None
        return self.save()

    def todos(self):
        return Todo.find_all(self.id)

    def blogs(self):
        return Blog.find_all(self.id)

    def comments(self):
        return Comment.find_all(self.id)


    def others(self):
        ms = self.all()
        u = None
        for m in ms:
            if m.id == self.id:
                u = m
        ms.remove(u)
        return ms
