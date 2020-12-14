import pickle
from collections import deque

def serialize(smth):
    return pickle.dumps(smth)

def deserialize(smth):
    return pickle.loads(smth)

class SomeClass:
    def __init__(self, name):
        self.name = name

    def __dict__(self):
        return {'name': self.name}

    def __str__(self):
        return f'SomeClass named {self.name}'

    def dance():
        return "dancin"


iterator = iter(range(5))
to_try = [open('1.txt', 'rb'), iter(range(5)), print, deque, SomeClass, SomeClass.dance]
for thing in to_try:

    try:
        serialize(thing)
        print("yes")
    except:
        print("no")
