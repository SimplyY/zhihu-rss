__author__ = 'yuwei'


import threading

class MyThread(threading.Thread):
    def __init__(self, threadname, fun, *args):
        threading.Thread.__init__(self, name=threadname)
        self.name = threadname
        self.fun = fun
        self.args = args

    def run(self):
        if len(self.args) == 1:
            self.fun(self.args[0])
        elif len(self.args) == 2:
            self.fun(self.args[0], self.args[1])
        elif len(self.args) == 3:
            self.fun(self.args[0], self.args[1], self.args[2])
