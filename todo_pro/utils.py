import time


def log(*args, **kwargs):
    f = '%Y %m %d %H:%M:%S'
    value = time.localtime(int(time.time()))
    t = time.strftime(f, value)

    print(t, *args, **kwargs)
