import inspect
from collections import deque
from Clean.Models import ParentTraceProxy, STR2TR, IsAcceptingProxy, ParentStoreProxy
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


def get_trace_v2(a_find_accepting_bfs, parent_proxy):
    result, tmp = a_find_accepting_bfs(parent_proxy)
    if result:
        trace = []
        intial = parent_proxy.initial()[0]
        while tmp != intial:
            # trace.append(tmp)
            trace.extend(tmp)
            tmp = parent_proxy.parents[tmp]
        trace.append(intial)
        trace.reverse()
        return trace


def bfs_for_accept(g, initial=None):
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        if at_start:
            if initial:
                neighbours = initial
            else:
                neighbours = g.initial()
            at_start = False
        else:
            conf = frontier.popleft()
            neighbours = g.next(conf)
        for n in neighbours:
            if g.is_accepting(n):
                return True, n
            if n not in known:
                known.add(n)
                frontier.append(n)
    return False, None


def bfs_for_reachable(g, start, end):
    known = set()
    frontier = deque()
    neighbours = [start]
    for n in neighbours:
        if n not in known:
            known.add(n)
            frontier.append(n)
    while frontier:
        neighbours = g.next(frontier.popleft())
        for n in neighbours:
            if n == end:
                return True
            if n not in known:
                known.add(n)
                frontier.append(n)
    return False


def finding_loop(g):
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontier.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                if bfs_for_reachable(g, n, n):
                    return True, n
            if n not in known:
                known.add(n)
                frontier.append(n)
    return False, None


def get_loop_trace(a_find_loop_bfs, parent_proxy, loop_node):
    result, final = a_find_loop_bfs(parent_proxy, loop_node)
    if result:
        trace = [final]
        tmp = parent_proxy.parents[final]
        while tmp != final:
            trace.append(tmp)
            tmp = parent_proxy.parents[tmp]
        trace.append(final)
        trace.reverse()
        return trace


def loop_model_checker(behavior_soup, is_accepted):
    str2tr = STR2TR(behavior_soup)
    a_accepting_proxy = IsAcceptingProxy(str2tr, is_accepted)
    a_parent_store = ParentStoreProxy(a_accepting_proxy)
    a_parent_store2 = ParentStoreProxy(a_accepting_proxy)
    trace = get_trace_v2(bfs_for_accept, a_parent_store)
    loop_node = finding_loop(a_parent_store)[1]
    loop_node = a_parent_store2.next(loop_node)
    loop_trace = get_loop_trace(bfs_for_accept, a_parent_store2, loop_node)
    return trace, loop_trace


def predicate_model_checker(transition_relation, predicate):
    print(f'{"-" * 50}\npredicate model-checking for:\n{inspect.getsource(predicate)}')

    op_tracer = ParentTraceProxy(transition_relation)

    [pred, found, count, target], known = predicate_finder(op_tracer, predicate)
    print(f'has reachable accepting state {found} after exploring ', count, ' configurations')

    if found is True:
        the_trace = get_trace(op_tracer.parents, target, op_tracer.roots())
        trace_string = f'-'.join(str(x) for x in the_trace)
        print(f'The trace is: \n{trace_string}')


def predicate_model_checker_v2(behavior_soup, is_accepted):
    str2tr = STR2TR(behavior_soup)
    a_accepting_proxy = IsAcceptingProxy(str2tr, is_accepted)
    a_parent_store = ParentStoreProxy(a_accepting_proxy)
    trace = get_trace_v2(bfs_for_accept, a_parent_store)
    return trace


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
