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

if __name__ == '__main__':
    h = HanoiConfiguration(3,3)
    pDict = {}
    ptp = ParentTraceProxy(h,pDict)
    [p,found,count,target] = predicate_finder(ptp,) #lambda function for Hanoi
    dict = {1:2 , 2:1, 3:1, 5:2, 6:2, 4:5 }
    print(get_trace(dict, 6))