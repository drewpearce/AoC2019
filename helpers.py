import os
import time


def load_inputs_lines(folder, file_name, out_type=None):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        folder,
        file_name
    )
    with open(path) as f:
        out = f.readlines()

    if out_type == 'int':
        out = [int(o) for o in out]

    return out


class Timer(object):
    def __init__(self):
        self.start_time = self.now()
        self.stop_time = None
        self.duration = None

    @staticmethod
    def now():
        return int(round(time.time() * 1000))

    def start(self):
        self.start_time = self.now()
        self.stop_time = None
        self.duration = None

    def stop(self):
        self.stop_time = self.now()
        self.duration = self.stop_time - self.start_time
