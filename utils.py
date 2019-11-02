import os
import time
from threading import RLock

lock = RLock()

class utils(object):
    def __init__(self, file_path):
        super(utils, self).__init__()

        self.file_path = file_path
        self.lock = lock

        self.patterns = {
            'R1' : '\033[31;1m', 'G1' : '\033[32;1m',
            'Y1' : '\033[33;1m', 'P1' : '\033[35;1m',
            'CC' : '\033[0m'
        }

    def terminal_size(self):
        data = {}
        data['columns'], data['lines'] = os.get_terminal_size()

        return data

    def real_path(self, file_name):
        return os.path.dirname(os.path.abspath(self.file_path)) + file_name

    def colors(self, value='', patterns='', remove=False):
        if not patterns:
            patterns = self.patterns

        for code in patterns:
            value = value.replace('[{}]'.format(code), patterns[code] if not remove else '')

        return value

    def banner(self, values, color='[G1]'):
        os.system('cls' if os.name == 'nt' else 'clear')
        for value in values:
            print(self.colors(f'{color}{value}'))
        print(self.colors('[CC]'))

    def xfilter(self, data):
        for i in range(len(data)):
            data[i] = data[i].strip()
            if data[i].startswith('#'):
                data[i] = ''

        return list(set([x for x in data if x]))

    def sleep_forever(self):
        while True:
            time.sleep(86400)
