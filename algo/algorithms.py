from algo.Traversal import predicate_finder
from model.Hanoi import HanoiConfiguration, HanoiRules
from model.Trace import ParentTraceProxy


def get_trace(dic, target):
    result, tmp = dict(target)
    if result:
        trace = []
        initial = target.initial()[0]
        while tmp != initial:
            trace.append(tmp)
            tmp = target.parents[tmp]
        trace.append(initial)
        trace.reverse()
        return trace

if __name__ == '__main__':
    hanoiConfiguration = HanoiConfiguration(nbTower=3,nbDisk=3)
    h = HanoiRules([hanoiConfiguration])

    # h = HanoiConfiguration(3,3)
    pDict = {}
    ptp = ParentTraceProxy(h, pDict)
    [p,found,count,target] = predicate_finder(ptp,None) #lambda function for Hanoi
    dict = {1:2 , 2:1, 3:1, 5:2, 6:2, 4:5 }
    print(get_trace(dict, 6))