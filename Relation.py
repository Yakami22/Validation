from abc import abstractmethod


class TransitionRelation:

    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class DictGraph(TransitionRelation):

    def roots(self):
        pass

    def next(self, source):
        pass


class NBits(TransitionRelation):
    def roots(self):
        pass

    def next(self, source):
        pass
