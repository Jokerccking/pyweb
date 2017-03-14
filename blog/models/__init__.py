import json
from utils import log

def load(path):
    """
    use json moudle get content in the file
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        if s == '':
            s = '[]'
        return json.loads(s)


def save(data,path):
    """
    save data into file by json moudle
    """
    data = json.dumps(data, ensure_ascii=False, indent=2)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(data)


class Model(object):
    """
    base data Class for storing message
    """
    @classmethod
    def data_path(cls):
        name = cls.__name__
        return 'data/{}.txt'.format(name)

    @classmethod
    def new(cls, form):
        m= cls(form)
        return m.save()

    @classmethod
    def all(cls):
        path = cls.data_path()
        return [cls(m) for m in load(path)]

    @classmethod
    def find(cls, i):
        ms = cls.all()
        mod = None
        for m in ms:
            if m.id == i:
                mod = m
        return mod

    @classmethod
    def pop(cls, i):
        ms = cls.all()
        log('ms :: i::',ms,i)
        mod = None
        for index,obj in enumerate(ms):
            log('obj', obj, obj.id)
            if obj.id == i:
                mod = ms.pop(index)
                log('mod', mod)
                p = [m.__dict__ for m in ms]
                save(p, cls.data_path())
        log('pop::::',mod)
        return mod


    def __repr__(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__.copy()

    def save(self):
        ms = self.all()
        if self.id is None:
            i = 0
            if len(ms) > 0:
                i = ms[-1].id + 1
            self.id = i
            ms.append(self)
        else:
            for index,obj in enumerate(ms):
                if obj.id == self.id:
                    ms[index] = self
        p = [m.__dict__ for m in ms]
        save(p, self.data_path())
        return self

