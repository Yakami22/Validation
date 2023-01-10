from abc import ABC, abstractmethod

class TransitionRelation(ABC):
    #abstract method
    @abstractmethod
    def roots(self) :
        pass

    @abstractmethod
    def next(self , source):
        pass




class DictGraph(TransitionRelation):
    def roots(self) :
        pass

    def next(self , source):
        pass


class Nbits(TransitionRelation):
    pass