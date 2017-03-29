import os

import requests
from pyquery import PyQuery


class Model(object):
    """
    基类： 用于显示信息
    """
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{} = ({})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{} \n  {}>'.format(name, '\n  '.join(properties))


class Movie(Model):
    """
    存储电影信息
    """
    def __init__(self):
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def cached_url(url):
    """
    缓存：避免重复下载网页，浪费资源
    :param url:
    :return:
    """
    folder = 'cached'
    filename = url.split('=', 1)[-1] + '.html'
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        # 建立cached文件夹
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


def movie_from_div(div):
    """
    从一个 div 里面获取到一个电影信息
    :param div:
    :return:
    """
    e = PyQuery(div)

    # 小作用域变量用单字符
    m = Movie()
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()

    return m


def movies_form_url(url):
    """
    从 url 中下载网页并解析出页面所有电影
    :param url:
    :return:
    """
    page = cached_url(url)

    e = PyQuery(page)
    items = e('.item')
    movies = [movie_from_div(i) for i in items]
    return movies


# def cached_image(m):
#     folder = 'img'
#     name = m.cover_url.split("/")[-1]
#     filename = os.path.join(folder, name)
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     headers = {
#         'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
#     }
#     # 发送网络请求, 把结果写入到文件夹中
#     r = requests.get(m.cover_url, headers)
#     with open(filename, 'wb') as f:
#         f.write(r.content)


def main():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_form_url(url)
        # for m in movies:
        #     cached_image(m)


if __name__ == '__main__':
    main()
