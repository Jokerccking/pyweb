from models import Model
from time import time

class Todo(Model):
    @classmethod
    def complete(cls):
        pass

    @classmethod
    def update(cls):
        pass

    def __init__(self, form):
        self.id = None
        self.uid = form.get('uid')
        self.ct = int(time.time())
        self.ut = self.ct
        self.completed = False
