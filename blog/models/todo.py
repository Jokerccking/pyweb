from models import Model
from time import time

class Todo(Model):
    def __init__(self, form):
        self.id = None
        self.uid = form.get('uid')
        self.cotent = form.get('content','')
        self.ct = int(time.time())
        self.ut = self.ct
        self.completed = False

    def complete(self):
        self.completed = True

    def update(self, content):
        self.ut = int(time.time())
        self.content = content

