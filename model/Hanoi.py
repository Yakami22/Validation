import copy

from model.TransitionRelation import TransitionRelation


class HanoiConfiguration:
    def __init__(self, nbTower: int, nbDisk: int):
        self.nbTower = nbTower
        self.nbDisk = nbDisk
        self.towers = []

        for i in range(self.nbTower):
            self.towers.append([])

        for i in range(self.nbDisk):
            self.towers[0].append(self.nbDisk - i)

    def __str__(self):
        return str(self.towers)


class HanoiRules(TransitionRelation):
    def __init__(self, roots: list):
        super().__init__(roots)

    def getRoots(self):
        pass

    def next(self, source):
        les_configs = []
        print("config original")
        print(source)

        if source not in les_configs:
            les_configs.append(source)

        resultat = copy.deepcopy(source)

        for i in range(len(source)):
            # len(source) = num des pegs
            resultat = copy.deepcopy(source)
            if resultat[i]:
                disk = resultat[i].pop()

                for j in range(len(source)):

                    # if i!=j and (not resultat[j] or resultat[j][-1]> disk):
                    #     temp = copy.deepcopy(resultat)
                    #     temp[j].append(disk)

                    if i != j and (not resultat[j]):
                        temp = copy.deepcopy(resultat)
                        temp[j].append(disk)

                        les_configs.append(temp)
                    elif i != j and resultat[j][-1] > disk:
                        temp = copy.deepcopy(resultat)
                        temp[j].append(disk)
                        les_configs.append(temp)

        print("list of all neighbours")
        print(les_configs)


if __name__ == '__main__':
    config = HanoiConfiguration(3, 4)
    print(config)
