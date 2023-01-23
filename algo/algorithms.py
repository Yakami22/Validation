from algo.Traversal import predicate_finder
from model.Hanoi import HanoiConfiguration
from model.Trace import ParentTraceProxy


def get_trace(dict, target):
    # result, tmp = dict(target)
    # if result:
    #     trace = []
    #     initial = target.initial()[0]
    #     while tmp != initial:
    #         trace.append(tmp)
    #         tmp = target.parents[tmp]
    #     trace.append(initial)
    #     trace.reverse()
    #     return trace
    trace = [target]
    current = target
    while current != dict[current]:
        current = dict[trace[-1]]
        trace.append(current)
    trace.reverse()
    return trace

