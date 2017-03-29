import os

from pyquery import PyQuery
from selenium import webdriver

driver = webdriver.PhantomJS()


class Model(object):
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{} = ({})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{} \n {}>'.format(name, '\n'.join(properties))


class RecommendItem(Model):
    """
    储存推荐商品
    """
    def __init__(self):
        self.title = ''
        self.cover_url = ''
        self.abstract = ''


def cached_url(url):
    """
    缓存，避免重复下载
    :param url:
    :return:
    """
    folder = 'cached'
    filename = url.rsplit('/')[-2] + '.html'
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        driver.get(url)
        with open(path, 'wb') as f:
            f.write(driver.page_source.encode())
        content = driver.page_source
        return content


def item_from_div(div):
    e = PyQuery(div)
    m = RecommendItem()
    m.abstract = e('.post_box_main .text').text()
    m.name = e('.title_box a').text()
    m.cover_rul = e('.post_box_img img').attr('src')
    return m


def item_from_url(url):
    page = cached_url(url)
    e = PyQuery(page)
    items = e('.post_box')
    return [item_from_div(i) for i in items]


def main():
    # items = item_from_url('http://zhizhizhihizhizhi.com/gn/1/')
    for i in range(0, 10):
        items = item_from_url('http://zhizhizhi.com/gn/{}/'.format(i))
        print(items)
    driver.close()


if __name__ == '__main__':
    main()
