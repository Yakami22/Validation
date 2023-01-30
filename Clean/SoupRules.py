import copy

from Clean.Algorithms import predicate_model_checker
from Clean.Models import STR2TR, SemanticTransitionRelations


class Behavior:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Behavior):
            return False
        return self.name == other.name and self.guard == other.guard and self.action == other.action

    def __str__(self):
        return self.name


class BehaviorSoup:
    def __init__(self, initial):
        self.initial = initial
        self.behaviors = []

    def add(self, name, guard, action):
        self.behaviors.append(Behavior(name, guard, action))

    def extend(self, beh):
        if isinstance(beh, Behavior):
            self.behaviors.append(beh)
        else:
            self.behaviors.extend(beh)


class BehaviorSoupSemantics(SemanticTransitionRelations):

    def __init__(self, prog):
        super().__init__()
        self.program = prog

    def initial(self):
        return [self.program.initial]

    def actions(self, configuration):
        return list(map(lambda ga: ga.action, filter(lambda ga: ga.guard(configuration), self.program.behaviors)))

    def execute(self, action, configuration):
        target = copy.deepcopy(configuration)
        print(action)
        action(target)
        return [target]


def soup_predicate_model_checker(soup_program, predicate):
    semantics = BehaviorSoupSemantics(soup_program)
    transition_relation = STR2TR(semantics)
    predicate_model_checker(transition_relation, predicate)
