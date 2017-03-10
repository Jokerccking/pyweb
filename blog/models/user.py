from models import Model
from user import User
from blog import Blog

class User(Model):
    def __init__(self):
        self.id = None
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.role = 10

    def validate_login(self):
        pass

    def validate_register(self):
        pass

    def todos(self):
        pass

    def blogs(self):
        pass
