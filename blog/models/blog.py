from models import Model
from time import time

class Blog(Model):
    def __init__(self, form):
        self.id = None
        self.uid = form.get('uid')
        self.content = form.get('content', '')
        self.ct = int(time.time())
        self.ut = self.ct

    def json(self):
        pass

    def update(self):
        pass

    def comments(self):
        pass


class Comment(Model):
    def __init__(self, form):
        self.id = None
        self.cotent = form.get('content', '')
        self.bid = form.get('bid', '')
        self.ct = int(time.time())

    def json(self):
        pass

