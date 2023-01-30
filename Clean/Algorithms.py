import inspect

from Clean.DictGraph import DictGraph
from Clean.Models import ParentTraceProxy
from Clean.Traversal import predicate_finder


def get_trace(parents, n, i):
    trace = [n]
    try:
        parent = parents[n]
    except KeyError:
        parent = None
    if isinstance(parent, list):
        parent = parent[0] if len(parent) > 0 else None
    while parent is not None:
        trace.append(parent)
        if parent in i:
            return trace
        try:
            parent = parents[parent]
            if isinstance(parent, list):
                parent = parent[0] if len(parent) > 0 else None
        except KeyError:
            parent = None
    return trace


def predicate_model_checker(transition_relation, predicate):
    print(f'{"-" * 50}\npredicate model-checking for:\n{inspect.getsource(predicate)}')

    op_tracer = ParentTraceProxy(transition_relation)

    [pred, found, count, target], known = predicate_finder(op_tracer, predicate)
    print(f'has reachable accepting state {found} after exploring ', count, ' configurations')

    if found is True:
        the_trace = get_trace(op_tracer.parents, target, op_tracer.roots())
        trace_string = f'\n{"-" * 20}\n'.join(str(x) for x in the_trace)
        trace_string = f'-'.join(str(x) for x in the_trace)
        print(f'The trace is: \n{trace_string}')


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

    print('-------------- Traces for different values in our graph --------------')
    n = 2
    print("The trace to get to " + str(n) + " is : " + str(get_trace(g, n, [1, 2])))

    n = 1
    print("The trace to get to " + str(n) + " is : " + str(get_trace(g, n, [2, 6])))

    n = 4
    print("The trace to get to " + str(n) + " is : " + str(get_trace(g, n, [2, 5])))

    n = 6
    print("The trace to get to " + str(n) + " is : " + str(get_trace(g, n, [2, 5])))
