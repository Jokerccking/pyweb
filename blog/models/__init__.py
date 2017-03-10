import json

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read
        return json.load(s)


def save(path, data):
    data = json.dumps(data, ensuer_ascii=Fale, indent=2)
    with open(data, 'w+', encoding='utf-8') as f:
        f.write(data)


class Model(object):
    """
    """
    @classmethod
    def data_path(cls):
        pass

    @classmethod
    def new(cls, form):
        m= cls(form)
        m.save()
        return m

    @classmethod
    def all(cls):
        ms = cls.


    @classmethod
    def find_by(cls, **kwargs):
        pass

    @classmethod
    def find_all(cls, **kwargs):
        pass

    @classmethod
    def pop(cls, i):
        pass

    def __repr__(self):
        ms = self.all()
        pass

    def json(self):
        pass

    def save(self):
        pass

