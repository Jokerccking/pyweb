from models import Model
import time
from utils import log

class Todo(Model):
    #@classmethod
    #def find_all(cls,uid):
    #    ms = []
    #    tds = cls.all()
    #    for td in tds:
    #        if td.uid == uid:
    #            ms.append(td)
    #    return ms

    #@classmethod
    #def tid(cls, i):
    #    ms = cls.all()
    #    td = None
    #    for m in ms:
    #        if m.id == i:
    #            td = m
    #            break
    #    return td

    def __init__(self, form):
        self.id = form.get('id')
        self.uid = int(form.get('uid'))
        self.content = form.get('content','')
        self.ct = form.get('ct',int(time.time()))
        self.ut = form.get('ut',self.ct)
        self.completed = form.get('complete',False)


    def update(self,cnt):
        self.ut = int(time.time())
        self.content = cnt
        return self.save()

    def complete(self):
        self.completed = True
        return self.save()

