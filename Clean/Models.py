from abc import abstractmethod


class TransitionRelation:
    """
    A class that represents a contract
    """

    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class IdentityProxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class PreInitializedProxy(IdentityProxy):
    def __init__(self, operand, configurations):
        super().__init__(operand)
        self.configurations = configurations

    def initial(self):
        return self.configurations


class ParentStoreProxy(IdentityProxy):
    def __init__(self, operand):
        super().__init__(operand)
        self.parents = {}

    def next(self, config):
        neighs = self.operand.next(config)
        for n in neighs:
            if n not in self.parents:
                self.parents[n] = config
        return neighs


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, parents=None):
        super().__init__(operand)
        self.parents = {} if parents is None else parents

    def initial(self):
        neighbours = self.operand.initial()
        for n in neighbours:
            self.parents[n] = []
        return neighbours

    def next(self, configuration):
        neighbours = self.operand.next(configuration)
        for n in neighbours:
            if self.parents.get(n) is None:
                self.parents[n] = [configuration]
        return neighbours


class SemanticTransitionRelations:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, conf):
        pass

    def execute(self, conf, action):
        pass


class STR2TR(TransitionRelation):
    """
    Class to transform a STR object to a TR object
    """

    def __init__(self, str):
        self.operand = str

    def roots(self):
        return self.operand.initial()

    def initial(self):
        return self.operand.initial()

    def next(self, c):
        targets = []
        for a in self.operand.actions(c):
            target = self.operand.execute(a, c)
            targets.extend(target)
        return targets


class IsAcceptingProxy(IdentityProxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate

    def is_accepting(self, c):
        return self.predicate(c)
