__author__ = 'yuwei'


import threading

class MyThread(threading.Thread):
    def __init__(self, threadname, fun, *args):
        super().__init__(name=threadname)
        self.name = threadname
        self.fun = fun
        self.args = args

    def run(self):
        self.fun(*self.args)

