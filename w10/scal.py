import threading
from time import time
from random import randint


def scal_mul(v1, v2):
    res = 0
    for i, j in zip(v1, v2):
        res += i*j
    return res


lock = threading.Lock()
res = 0


def component_mul(x, y):
    global res
    lock.acquire()
    res += x*y
    lock.release()


def scal_mul_threads(v1, v2):
    for i in range(len(v1)):
        thread = threading.Thread(target = component_mul, args = (v1[i], v2[i]))
        thread.start()
    return res
    
    #coming soon...
