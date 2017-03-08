import ssl
import socket

protocol_port = {
    'http': 80,
    'https': 443,
}
def log(*args, **kwargs):
    print(*args, **kwargs)

def path_with_query(path, query):
    """

    """
    s = []
    for k, v in query.items():
        s.append("{}={}".format(k, v))
    que = "&".join(s)
    return path+'?'+que

def parse_url(url):
    """

    """
    protocol = 'http'
    if 'http://' in url:
        u = url.split('://')[1]
    elif 'https://' in url:
        u = url.split('://')[1]
        protocol = 'https'
    else:
        u = url

    # parse path
    if '/' in u:
        i = u.index('/')
        path = u[i:]
        h = u[:i]
    else:
        h = u
        path = '/'

    # pase host and port
    port = protocol_port[protocol]
    if ':' in h:
        host, port = h.split(':')
    else:
        host = h
    return protocol,host,port,path


def socket_by_protocol(protocol):
    if protocol=='http':
        return socket.socket()
    else:
        return ssl.wrap_socket(socket.socket())



def request_by_socket(s, host, path ):

    request = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(path, host)
    s.send(request.encode(encoding='utf-8'))


def response_by_socket(s):
    response = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break;
        response += r
    return response.decode('utf-8')


def parse_response(response):
    header, body = response.split('\r\n\r\n', 1)
    head = header.split('\r\n')
    status_code = int(head[0].split()[1])
    headers = {}
    for line in head[1:]:
        k,v = line.split(':', 1)
        headers[k] = v
    return status_code, headers, body

def parse_html(body):
    cn_name = ''
    en_name = ''
    score_num = 0
    interest_num = 0
    lines = body.splitlines()
    movie = []

    for line in lines:
        # parse movie name
        if '<span class="title">' in line:
            m = line.index('>') + 1
            n = line.rindex('<')
            if ';' in line:
                m += 13
                en_name = line[m:n]
            else:
                cn_name = line[m:n]
            continue

        #parse score
        if '<span class="rating_num" property="v:average">' in line:
            m = line.index('>') + 1
            n = line.rindex('<')
            score_num = float(line[m:n])
            continue

        # parse number of person
        if line.endswith('人评价</span>'):
            m = line.index('>') + 1
            n = line.rindex('<') -3
            interest_num = int(line[m:n])
            continue

        # parse quote,update list
        if '<span class="inq">' in line:
            m = line.index('>') + 1
            n = line.rindex('<')
            inq = line[m:n]
            movie.append((cn_name, en_name, score_num, interest_num, inq))

        return movie

def crawl(url, query):
    url = path_with_query(url, query)
    p, h, port, path = parse_url(url)
    s = socket_by_protocol(p)
    s.connect((h, port))
    request_by_socket(s, h, path)

    response = response_by_socket(s)
    status_code, headers, body = parse_response(response)

    if status_code in [301, 302]:
        return crawl(headers['Location'], query)

    return status_code, headers, body

def main():
    path = 'https://movie.douban.com/top250'
    movie = []
    for i in range(10):
        query = {
            'start': i*25,
        }
        status_code, headers, body = crawl(path,query)
        movie += parse_html(body)
    log(len(movie), movie)
    return movie


if __name__ == '__main__':
    main()

