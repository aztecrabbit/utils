import os
import time
from threading import RLock

lock = RLock()


class utils(object):
    def __init__(self, file_name):
        super(utils, self).__init__()

        self.file_name = file_name
        self.lock = lock

    def get_terminal_size(self) -> dict:
        terminal_size = {}
        terminal_size['columns'], terminal_size['lines'] = 256, 64

        try:
            terminal_size['columns'], terminal_size['lines'] = os.get_terminal_size()
        except Exception:
            pass

        return terminal_size

    def real_path(self, name: str = __file__) -> str:
        return os.path.dirname(os.path.abspath(self.file_name)) + name

    def colors(self, value: str, patterns: list = None) -> str:
        if not patterns:
            patterns = [
                ('R1', '\033[31;1m'), ('G1', '\033[32;1m'),
                ('Y1', '\033[33;1m'), ('P1', '\033[35;1m'), ('CC', '\033[0m'),
            ]

        for key, val in patterns:
            value = value.replace(f"[{key}]", val)

        return value

    def banner(self, values: str, color: str = '[G1]'):
        os.system('cls' if os.name == 'nt' else 'clear')
        for value in values:
            print(self.colors(f'{color}{value}'))
        print(self.colors('[CC]'))

    def xfilter(self, data_list: list) -> list:
        return list(set([x.strip() for x in data_list if x.strip() and not x.startswith('#')]))

    def sleep_forever(self):
        while True:
            time.sleep(86400)
