#import string
import zipfile
import os
import pathlib
import re

class TextLoader:
    def __init__(self, address):
        with zipfile.ZipFile('sample.zip','r') as sample:
            sample.extractall(address)
        self.path = pathlib.Path('sample')
        self.files = [file for file in list(self.path.glob('**/*')) if file.is_file()]
        self.iterable = iter(self.files)

    def __len__(self):
        return len(self.files)

    def __iter__(self):
        return self

    def __next__(self):
        curr_file = next(self.iterable)

        with curr_file.open('r', encoding = 'utf-8') as file:
            text = file.read()

        with curr_file.open('w', encoding = 'utf-8') as file:
            file.write(self.normalize(text))
        file = curr_file.open('r', encoding = 'utf-8')
        return file

    def normalize(self, text):
        text = re.sub(r'[^\w\s]', ' ', text)
        text = text.lower()
        return text

f = TextLoader('C:\\Users\\plutonium\\mipt_hw_py\\w9')
print(len(f))
for i in range(len(f)):
    g = next(f)
    print(g.read())
    print('next text')
