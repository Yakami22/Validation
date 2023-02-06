import inspect
from collections import deque

from Clean.Models import ParentTraceProxy, STR2TR, IsAcceptingProxy, ParentStoreProxy
from Clean.Traversal import predicate_finder


def get_trace_v2(afind_actepting_bfs, parentProxy):
    result, tmp = afind_actepting_bfs(parentProxy)
    if result:
        trace = []
        intial = parentProxy.initial()[0]
        while tmp != intial:
            trace.append(tmp)
            tmp = parentProxy.parents[tmp]
        trace.append(intial)
        trace.reverse()
        return trace

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


def find_accepting_bfs(g, initial=None):
    known = set()
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            if initial:
                neighbours = initial
            else:
                neighbours = g.initial()
            at_start = False
        else:
            conf = frontiere.popleft()
            neighbours = g.next(conf)
        for n in neighbours:
            if g.is_accepting(n):
                return True, n
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False, None


def find_loop(g):
    known = set()
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                if is_reachable_bfs(g, n, n):
                    return True, n
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False, None


def is_reachable_bfs(g, start, end):
    known = set()
    frontiere = deque()
    neighbours = [start]
    for n in neighbours:
        if n not in known:
            known.add(n)
            frontiere.append(n)
    while frontiere:
        neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if n == end:
                return True
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False


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

def predicate_model_checker_v2(behavior_soup, isAccepted):
    str2tr = STR2TR(behavior_soup)
    aAcceptingProxy = IsAcceptingProxy(str2tr, isAccepted)
    aParentStore = ParentStoreProxy(aAcceptingProxy)
    trace = get_trace_v2(find_accepting_bfs, aParentStore)
    return trace

def get_loop_trace(afind_loop_bfs, parentProxy, loopNode):
    result, final = afind_loop_bfs(parentProxy, loopNode)
    if result:
        trace = [final]
        tmp = parentProxy.parents[final]
        while tmp != final:
            trace.append(tmp)
            tmp = parentProxy.parents[tmp]
        trace.append(final)
        trace.reverse()
        return trace



def loop_model_checker(behavior_soup, isAccepted):
    str2tr = STR2TR(behavior_soup)
    aAcceptingProxy = IsAcceptingProxy(str2tr, isAccepted)
    aParentStore = ParentStoreProxy(aAcceptingProxy)
    aParentStore2 = ParentStoreProxy(aAcceptingProxy)
    trace = get_trace_v2(find_accepting_bfs, aParentStore)
    loopNode = find_loop(aParentStore)[1]
    loopNode = aParentStore2.next(loopNode)
    loop_trace = get_loop_trace(find_accepting_bfs, aParentStore2, loopNode)
    return trace, loop_trace


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
