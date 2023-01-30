from Clean.Algorithms import predicate_model_checker
from Clean.Models import TransitionRelation
from Clean.Traversal import predicate_finder


class NBits(TransitionRelation):

    def __init__(self, roots: list, n: int):
        self.initial = roots
        self.nBits = n

    def roots(self):
        return self.initial

    def next(self, source):
        neighbours = []
        for i in range(self.nBits):
            neighbours.append(source ^ (1 << i))
        return neighbours


def print_binary(s):
    return set(map(
        lambda x: "{0:03b}".format(x),
        s))


if __name__ == '__main__':

    x = 6
    [pred, found, count, target], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable, found: ', found, ' [', target, '] explored ', count, 'nodes, known: ', print_binary(known))

    x = 1
    [pred, found, count, target], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable, found: ', found, ' [', target, '] explored ', count, 'nodes, known: ', print_binary(known))

    x = 6
    predicate_model_checker(NBits([0], 3), lambda n: n == x)

    x = 1
    predicate_model_checker(NBits([0], 3), lambda n: n == x)