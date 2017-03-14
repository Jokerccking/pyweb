from models import Model
from time import time

class Blog(Model):
    @classmethod
    def bid(cls, bid):
        return cls.find(bid)

    def __init__(self, form):
        self.id = form.get('id')
        self.uid = form.get('uid')
        self.content = form.get('content', '')
        self.ct = int(time.time())
        self.ut = self.ct

    def to_dict(self):
        pass

    def update(self, content):
        self.ut = int(time.time())
        self.content = content

    def comments(self):
        return Comment.find_all(bid = self.id)


class Comment(Model):
    def __init__(self, form):
        self.id = None
        self.id = form.get('uid')
        self.bid = form.get('bid', '')
        self.cotent = form.get('content', '')
        self.ct = int(time.time())

    def json(self):
        pass

