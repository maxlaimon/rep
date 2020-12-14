import sys
import pickle
from binarytree import Node, build

def add(x):
    treelist.append(x)


def find(x):
    pass


def delete(x):
    treelist.remove(x)


def print(x):
    root = build(treelist)
    root.pprint()


def clear(x):
    treelist.clear()


def dump(x):
    with open('backup.pickle', 'wb') as f:
        pickle.dump(treelist, f)


def exit(x):
    sys.exit()


if __name__ == '__main__':
    global treelist

    try:
        with open('backup.pickle', 'rb') as f:
            treelist = pickle.load(f)
    except:
        treelist = []


    while True:
        command = list(input().split())
        cmd = command[0]
        try:
            x = int(command[1])
        except IndexError:
            x = None

        cmdlist = ['add', 'find', 'delete', 'print', 'clear', 'dump', 'exit']
        if cmd in cmdlist:
            exec(cmd + '(x)')
        else:
            print('idk')
