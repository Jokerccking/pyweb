from models import Model
import time
from utils import log

class Blog(Model):
    @classmethod
    def popi(cls,i):
        Comment.rm_bid(i)
        return cls.pop(i)


    def __init__(self, form):
        self.id = form.get('id')
        self.uid = int(form.get('uid'))
        self.content = form.get('content', '')
        self.ct = form.get('ct',int(time.time()))

    def comments(self):
        return Comment.find_bid(self.id)

    def to_dict(self):
        d = self.__dict__.copy()
        cms = [cm.to_dict() for cm in self.comments()]
        d['comments'] = cms
        return d


class Comment(Model):
    @classmethod
    def rm_bid(cls,bid):
        ms = cls.all()
        def f(m):
            if m.bid != bid:
                return True
        ms = filter(f,ms)
        cls.resave(ms)

    @classmethod
    def find_bid(cls,bid):
        cms = []
        ms = cls.all()
        for m in ms:
            if m.bid == bid:
                cms.append(m)
        return cms

    def __init__(self, form):
        self.id = form.get('id')
        self.bid = int(form.get('bid', ''))
        self.um = form.get('um')
        self.content = form.get('content', '')
        self.ct = form.get('ct', int(time.time()))

