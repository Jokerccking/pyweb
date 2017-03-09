import time


def log(*args, **kwargs):

    print(*args, **kwargs)


def current_time():
    f = '%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    return time.strftime(f, value)


def error(request, code=404):
    log('请求错误，找不到资源：：：', request)
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Not Found</h1>'
    }
    return e.get(code, b'')


def parse_path(path):
    query = {}
    if '?' in path:
        path, q = path.split('?')
        qs = q.split('&')
        for e in qs:
            k, v = e.split('=')
            query[k] = v
    return path, query


def parse_cookies(headers):
    cookies = {}
    cks = headers.get('Cookie')
    if cks is not None:
        cks = cks.split('; ')
        for ck in cks:
            k, v = ck.split('=')
            cookies[k.strip()] = v.strip()
    return cookies


def parse_headers(rh):
    headers = {}
    li = rh.split('\r\n')
    for e in li:
        k, v = e.split(':', 1)
        headers[k] = v
    return headers


# def test_ct():
#     log(current_time())
#
# if __name__ == '__main__':
#     test_ct()
