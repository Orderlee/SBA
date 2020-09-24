import sys
sys.path.insert(0, '/users/YoungWoo/SBA')
from cabage.entity import Entity
from cabage.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self):
        pass

    def modeling(self):
        pass

    def learning(self):
        pass

    def submit(self):
        pass
