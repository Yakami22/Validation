from abc import abstractmethod

class TransitionRelation:

    @abstractmethod
    def getRoots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass

