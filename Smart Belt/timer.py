import time

class TicToc:
    def __init__(self, delay = 4):
        self.tic = time.time()
        self.toc = time.time()
        self.delay = delay

    def setTic(self):
        self.tic = time.time()

    def setToc(self):
        self.toc = time.time()

    def getTic(self):
        return self.tic

    def getToc(self):
        return self.toc
    
    def setDelay(self, delay):
        self.delay = delay

    def diff(self):
        return self.tic - self.toc

    def canScore(self):
        return True if self.diff() > self.delay else False