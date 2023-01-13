from algo.Traversal import predicate_finder
from model.Hanoi import HanoiConfiguration
from model.Trace import ParentTraceProxy


def get_trace(dic, target):
    result, tmp = dict(target)
    if result:
        trace = []
        intial = target.initial()[0]
        while tmp != intial:
            trace.append(tmp)
            tmp = target.parents[tmp]
        trace.append(intial)
        trace.reverse()
        return trace

if __name__ == '__main__':
    h = HanoiConfiguration(3,3)
    pDict = {}
    ptp = ParentTraceProxy(h,pDict)
    [p,found,count,target] = predicate_finder(ptp,)