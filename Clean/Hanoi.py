import copy

from Models import TransitionRelation
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


hanoi = HanoiConfiguration(3, 3)
initial = hanoi.initial()
print('Graph initial: {}'.format(initial))
nextHanoi = hanoi.next(initial)
print('Next config : {}'.format(nextHanoi))

print('Le next de  : {} est  : {}'.format(nextHanoi[0], hanoi.next(nextHanoi[0])))

print('Le next de  : {} est  : {}'.format(nextHanoi[1], hanoi.next(nextHanoi[1])))

print('Le next de  : {} est  : {}'.format(nextHanoi[2], hanoi.next(nextHanoi[2])))
