from models import Model
import time
from utils import log

class Blog(Model):
    def __init__(self, form):
        self.id = form.get('id')
        self.uid = int(form.get('uid'))
        self.content = form.get('content', '')
        self.ct = form.get('ct',int(time.time()))
        self.ut = form.get('ut',self.ct)

    def comments(self):
        cms = []
        ms = Comment.all()
        for m in ms:
            if m.bid == self.id:
                cms.append(m)
        return cms


class Comment(Model):
    def __init__(self, form):
        self.id = None
        self.uid = form.get('uid')
        self.bid = form.get('bid', '')
        self.cotent = form.get('content', '')
        self.ct = form.get('ct', int(time.time()))

