from model.TransitionRelation import TransitionRelation


class NBits(TransitionRelation):

    def __init__(self, roots: list, n: int):
        # super().__init__(roots)
        self.nBits = n

    def getRoots(self):
        return self.roots

    def next(self, source):
        neighbours_list = []
        for i in range(self.nBits):
            neighbours_list.append(source ^ (1 << i))
        return neighbours_list

    def next_bis(self, source):
        resultat = []
        test = []
        print("source")
        print(source)
        if source not in test:
            test.append(source)
        resultat = source.copy()

        for i in range(len(source)):

            resultat = source.copy()

            if (resultat[i] == 0):
                resultat[i] = 1
            else:
                resultat[i] = 0

            print("neighbour ")
            print(resultat)
            if resultat not in test:
                test.append(resultat)

        print("list of neighbours in binary ")
        print(test)
