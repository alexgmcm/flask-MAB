import numpy as np
class Cat:

    def __init__(self,name):
        self.score = 0
        self.views= 0
        self.name = name
        self.fails = 0


    def vote(self):
        self.score = self.score + 1


    def view(self):
        self.views = self.views + 1

    def fail(self):
        self.fails = self.fails + 1

    def drawBeta(self):
        return np.random.beta(1+self.score,1+self.fails)

    
