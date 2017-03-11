import time

def log(*args, **kwargs):
    f = '%Y/%m/%d'
    t = time.localtime(int(time.time()))
    print(time.strftime(f, t), *args, **kwargs)


