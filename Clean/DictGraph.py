from Clean.Helper import print_found_message
from Clean.Models import TransitionRelation
from Clean.Traversal import bfs, predicate_finder


class DictGraph(TransitionRelation):
    def __init__(self, ini, graph):
        self.initials = ini
        self.graph = graph

    def roots(self):
        return self.initials

    def next(self, source):
        try:
            return self.graph[source]
        except KeyError:
            return []


if __name__ == '__main__':
    g = {
        0: [1, 3, 5],
        1: [2],
        2: [0],
        3: [3, 4],
        4: [1, 2],
        5: [],
        6: []
    }


    def entry_function(s, n, a):
        # increment the count
        a[2] += 1
        # is the current node equal to the target ?
        a[1] = a[0] == n
        # return true if target found
        return a[1]


    graph1 = DictGraph([0], g)
    graph2 = DictGraph([0, 6], g)

    print('-------------------------------------------------- Test with graph 1 '
          '--------------------------------------------------')

    [target, found, count], known = bfs(graph1, [3, False, 0], on_entry=entry_function)
    print(print_found_message(found), 'Number of node explored :', count, 'Known : ', known)

    [target, found, count], known = bfs(graph1, [5, False, 0], on_entry=entry_function)
    print(print_found_message(found), 'Number of node explored :', count, 'Known : ', known)

    print('\n-------------------------------------------------- Test with graph 2 '
          '--------------------------------------------------')

    [target, found, count], known = bfs(graph2, [3, False, 0], on_entry=entry_function)
    print(print_found_message(found), 'Number of node explored :', count, 'Known : ', known)

    [target, found, count], known = bfs(graph2, [5, False, 0], on_entry=entry_function)
    print(print_found_message(found), 'Number of node explored :', count, 'Known : ', known)

    print('\n-------------------------------------------------- Test with predicate finder '
          '------------------------------------------')

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 3)
    print('pred(' + str(target) + ') =', found, 'Number of node explored :', count, 'Known : ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 5)
    print('pred(' + str(target) + ') =', found, 'Number of node explored :', count, 'Known : ', known)
