from algo.Traversal import predicate_finder
from algo.algorithms import get_trace
from model.Hanoi import HanoiConfiguration
from model.Trace import ParentTraceProxy

if __name__ == '__main__':
    h = HanoiConfiguration(3, 3)
    pDict = {}
    ptp = ParentTraceProxy(h, pDict)
    [p, found, count, target] = predicate_finder(ptp, )  # lambda function for Hanoi
    dico = {1: 2, 2: 1, 3: 1, 5: 2, 6: 2, 4: 5}
    print(get_trace(dico, 6))
