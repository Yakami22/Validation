import copy

from model.SemanticTransitionRelation import SemanticTransitionRelation


class BehaviorSoup:
    def __init__(self, conf):
        self.initial = conf
        self.behaviors = []

    def add(self, name, guard, action):
        self.behaviors.append(Behavior(name, guard, action))


class Behavior:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class BehaviourSoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.soup = program

    def initial(self):
        return[self.soup.initial]

    def actions(self, conf):
        return list(map(lambda beh: beh.action, filter(lambda beh: beh.guard(conf), self.soup.behaviors)))

    def execute(self, c, a):
        target = copy.deepcopy(c)
        r = a(target)
        return target
