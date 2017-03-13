from models import Model
import time

class Todo(Model):
    @classmethod
    def find_all(cls,uid):
        ms = []
        tds = cls.all()
        for td in tds:
            if td.uid == uid:
                ms.append(td)
        return ms

    def __init__(self, form):
        self.id = None
        self.uid = int(form.get('uid'))
        self.cotent = form.get('content','')
        self.ct = int(time.time())
        self.ut = self.ct
        self.completed = False

    def complete(self):
        self.completed = True

    def update(self, content):
        self.ut = int(time.time())
        self.content = content

