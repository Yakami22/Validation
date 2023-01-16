from abc import abstractmethod
import copy


class TransitionRelation:

    @abstractmethod
    def getRoots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass
