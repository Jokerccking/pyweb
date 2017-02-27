import json


def save(data, path):
    """
    序列化数据并保存
    :param data:
    :param path:
    :return:
    """
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(s)


def load(path):
    """
    从文件中加载数据并序列化后返回
    :param path:
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        if s is '':
            s = '[]'
        return json.loads(s)


class Model(object):
    """
    一个保存数据的基类
    """

    @classmethod
    def db_path(cls):
        """
        返回该类对应在数据库中的文件路径
        :return:
        """
        n = cls.__name__
        return 'db/{}.txt'.format(n)

    @classmethod
    def new(cls, form):
        """
        创建一个该类的实例
        :param form:
        :return:
        """
        return cls(form)

    @classmethod
    def all(cls):
        """
        返回该类的所有实例组成的列表
        :return:
        """
        models = load(cls.db_path())
        return [cls.new(m) for m in models]

    @classmethod
    def find_by(cls, **kwargs):
        """
        根据属性值从数据库找出第一个匹配的对象
        :param kwargs:
        :return:
        """
        mod = None
        ms = cls.all()
        tup = list(kwargs.items())[0]
        for m in ms:
            for item in m.__dict__.items():
                if item == tup:
                    mod = m
                    break
            if mod is not None:
                break
        return mod

    @classmethod
    def find_all(cls, **kwargs):
        """
        找出数据库中所有匹配的对象，以列表返回
        :return:
        """
        mods = []
        tup = list(kwargs.items())[0]
        ms = cls.all()
        for m in ms:
            for item in m.__dict__.items():
                if item == tup:
                    mods.append(m)
                    break
        return mods

    def save(self):
        """
        把对象的所有属性和值保存到数据库对应的文件中
        :return:
        """
        ms = self.all()
        if hasattr(self, 'id'):
            if self.id is None:
                i = 0
                if len(ms) > 0:
                    i = getattr(ms[-1], 'id') + 1
                setattr(self, 'id', i)
                ms.append(self)
            else:
                m = self.find_by(id=self.id)
                ms[ms.index(m)] = self
        properties = [m.__dict__ for m in ms]
        save(properties, self.db_path())
        return properties

    def remove(self):
        """
        从数据库中删除该对象的属性值
        :return:
        """
        ms = self.all()
        i = getattr(self, 'id')
        if i is not None:
            m = self.find_by(id=i)
            ms.remove(m)
        properties = [m.__dict__ for m in ms]
        save(properties, self.db_path())

    def __repr__(self):
        """
        重写对象的字符串表达形式
        :return:
        """
        n = self.__class__.__name__
        properties = '\n'.join(['{}:({})'.format(k, v) for k, v in self.__dict__.items()])
        return '< {}\n{} >\n'.format(n, properties)