import os

# from selenium import webdriver
import requests
from pyquery import PyQuery
# driver = webdriver.PhantomJS()


class Model(object):
    """
    基类, 用来显示类的信息
    """
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Mt(Model):
    def __init__(self):
        self.name = ''
        self.cover = ''
        self.imgs = []


def cached_page(url):
    folder = 'cached'
    filename = '_'.join(url.split('/')[-3:])
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求
        r = requests.get(url, headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def cached_list(url):
    folder = 'cached_list'
    filename = url.split('/')[-1]
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求
        r = requests.get(url, headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def mts_from_url(url):
    mts = []
    e = PyQuery(cached_list(url))
    urls = [PyQuery(i)('a').attr('href') for i in e('a.pimg')]
    print(urls)
    for u in urls:
        ul = 'http://www.rosiok.com' + u
        mt = Mt()
        q = PyQuery(cached_page(ul))
        mt.name = q('.don_box > img').attr('alt')
        mt.cover = q('.don_box > img').attr('src')
        mt.imgs = [PyQuery(i)('img').attr('src') for i in q('.a')]
        mts.append(mt)
    return mts


def save_cover(url):
    folder = 'img_cover'
    filename = '_'.join(url.split('/')[-3:])
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open('path', 'rb') as f:
            return f.read()
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求
        r = requests.get(url, headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def save_images(url):
    folder = 'imgs'
    filename = '_'.join(url.split('/')[-3:])
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        pass
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求
        r = requests.get(url, headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def main():
    for i in range(1, 24):
        url = 'http://www.rosiok.com/shipin/list_10_{}.html'.format(i)
        for mt in mts_from_url(url):
            print(mt)
            try:
                save_cover(mt.cover)
                for ul in mt.imgs:
                    save_images(ul)
            except:
                print('save image error')


if __name__ == '__main__':
    main()
