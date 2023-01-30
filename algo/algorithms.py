from algo.Traversal import predicate_finder
from model.Hanoi import HanoiConfiguration, HanoiRules
from model.Trace import ParentTraceProxy


def get_trace(dic, target):
    res=[target]
    courant=target
    while courant!=dic[courant]:
        courant=dic[res[-1]]
        res.append(courant)
        #print(courant.conf)
    res.reverse()
    return res


if __name__ == '__main__':
    hanoiConfiguration = HanoiConfiguration(nbTower=3,nbDisk=3)
    h = HanoiRules([hanoiConfiguration])

    # h = HanoiConfiguration(3,3)
    # pDict = {}
    # ptp = ParentTraceProxy(h, pDict)
    # [p,found,count,target] = predicate_finder(ptp,None) #lambda function for Hanoi
    dic = {1:2 , 2:1, 3:1, 5:2, 6:2, 4:5 }
    gra = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
    }
    print("im here ")
    dic = {1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 4: 5}
    print(get_trace(dic, 6))
    print("done")