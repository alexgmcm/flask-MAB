class Cat:

    def __init__(self,name):
        self.score = 0
        self.views= 0
        self.name = name


    def vote(self):
        self.score = self.score + 1

    def view(self):
        self.views = self.views + 1
