import copy

from Clean.Models import ParentTraceProxy, STR2TR
from Clean.SoupRules import BehaviorSoup, BehaviorSoupSemantics
from Clean.Traversal import predicate_finder



class AliceBob:

    def __init__(self):

        self.conf = [[1], [], [2]]
        # on fait la meme chose que hanoi

    def configuration(self):
        return self.conf


    def AB_on_entry(self, n):
        return len(n.conf[1])>=2




def guard(i, j):
    def res(config):
        if i == j :
            return False
        if config.conf[i] == []: # section vide
            return False
        elif i==0 or i==2:
            if j!=1:
                return False
            else :
                return True
        elif i == 1:
            if config.conf[i][0] == 2 and j != 2:
                return False
            if config.conf[i][0] == 1 and j != 0:
                return False
        else :
            return True
    return res


def action(i, j):
    def res(config):
        indice = config.conf[i].pop(0)
        config.conf[j].append(indice)
        return config

    return res



conf = AliceBob()
iC = conf

    # générer les règles pour AliceBob
prog = BehaviorSoup(iC)
for i in range(3):
    for j in range(3):
        if i != j:
            prog.add('{} vers {}'.format(i, j), guard(i, j), action(i, j))

for k in range(len(prog.behaviors)):
    print(prog.behaviors[k])
s = BehaviorSoupSemantics(prog)
translater = STR2TR(s)

