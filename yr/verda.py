#!/usr/bin/env python3

import os.path
import gzip

class Verda(): # <~ Norwegian: 'Verda' is English: 'World' ;)

    script_directory = os.path.dirname(os.path.abspath(__file__)) # directory of the script
    directory = 'locations'
    encoding = 'utf-8'

    def __init__(self):
        self.filename = os.path.join(self.script_directory, self.directory, 'verda.gz')

    def search(self, text=''):
        with gzip.open(self.filename, mode='r') as f:
            for row in f.readlines():
                row = row.decode(self.encoding).strip()
                if text in row:
                    yield row.split('\t')[-1][23:-13]

if __name__ == '__main__':
    print(list(Verda().search('Prague')))
