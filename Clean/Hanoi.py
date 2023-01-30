import copy

from Clean.SoupRules import BehaviorSoup, BehaviorSoupSemantics, Behavior
from Models import TransitionRelation, IdentityProxy, STR2TR


class HanoiConfiguration(TransitionRelation):
    def __init__(self, nb_tower: int, nb_disk: int):
        self.nbTower = nb_tower
        self.nbDisk = nb_disk
        self.towers = []

    def initial(self):
        return [[(self.nbDisk - i) for i in range(self.nbDisk)]] + [[] for _ in range(self.nbTower - 1)]

    def next(self, source):

        next_states = []
        if source not in next_states:
            next_states.append(source)

        for i in range(self.nbTower):
            results = copy.deepcopy(source)
            if results[i]:
                disk = results[i].pop()
                for j in range(self.nbTower):
                    if i != j and (not results[j] or results[j][-1] > disk):
                        temp = copy.deepcopy(results)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states




def hanoi_soap(nbStacks, nbDisks):
    i_conf = HanoiConfiguration(nbStacks, nbDisks)
    soup = BehaviorSoup(i_conf)
    for i in range(nbStacks):
        for j in range(nbStacks):
            soup.add(f'{i}-{j}', guarde_def(i, j), action_def(i, j))
    return soup


def guarde_def(i, j):
    def res(config):
        if config.conf[i] == []:
            return False
        indice = config.conf[i][0]
        if config.conf[j] == []:
            return True
        if config.conf[j][0] > indice:
            return True
        else:
            return False

    return res


def action_def(i, j):
    def res(config):
        indice = config.conf[i].pop(0)
        config.conf[j] = [indice] + config.conf[j]
        return config

    return res


def soup_hanoi(nbStacks, nbDisks):
    hanConf = HanoiConfiguration(nbStacks, nbDisks)
    iC = hanConf
    prog = BehaviorSoup(iC)

    for i in range(3):
        for j in range(3):
            if i != j:
                prog.add('Déplacer disque de la tour Num {} vers tour num {}'.format(i, j), guarde_def(i, j), action_def(i, j))
    for k in range(len(prog.behaviors)):
        print(prog.behaviors[k])

if __name__ == '__main__':

    hanoi = HanoiConfiguration(3, 3)
    initial = hanoi.initial()
    # print('Graph initial: {}'.format(initial))
    nextHanoi = hanoi.next(initial)
    # print('Next config : {}'.format(nextHanoi))
    #
    # print('Le next de  : {} est  : {}'.format(nextHanoi[0], hanoi.next(nextHanoi[0])))
    #
    # print('Le next de  : {} est  : {}'.format(nextHanoi[1], hanoi.next(nextHanoi[1])))
    #
    # print('Le next de  : {} est  : {}'.format(nextHanoi[2], hanoi.next(nextHanoi[2])))


#-----------------

soup_hanoi(3,3)