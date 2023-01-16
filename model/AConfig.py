from abc import abstractmethod

class AConfig:
    @abstractmethod
    def copy():
        pass


class C1(AConfig):
    def __init__(self, x):
        self.x = x
    
    def copy():
        # return C1(self.x)
        return