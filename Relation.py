from abc import abstractmethod
import copy

class TransitionRelation:

    def __init__(self, roots: list):
        self.roots = roots
        pass

    @abstractmethod
    def getRoots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class DictGraph(TransitionRelation):

    def __init__(self, roots: list):
        super().__init__(roots)

    def __init__(self, roots: dict, entry : list):
        super().__init__(roots)
        self.entry = entry

    def getRoots(self):
        return self.entry

    def next(self, source):
        return self.roots[source]


class NBits(TransitionRelation):

    def __init__(self, roots: list, n: int):
        super().__init__(roots)
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
            
            if (resultat[i] == 0 ): 
                resultat[i] = 1
            else: resultat[i] = 0
            
            print("neighbour ")
            print(resultat)
            if resultat not in test:
                test.append(resultat)
        
        print("list of neighbours in binary ")
        print(test)
    



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

                    if i!=j and (not resultat[j]) :
                        temp = copy.deepcopy(resultat)
                        temp[j].append(disk)

                        les_configs.append(temp)
                    elif i!=j and resultat[j][-1]> disk:
                        temp = copy.deepcopy(resultat)
                        temp[j].append(disk)
                        les_configs.append(temp)

        print("list of all neighbours")
        print(les_configs)

if __name__ == '__main__':
    graph = NBits([0, 0, 0], 3)
    myHanoi = HanoiRules([[3,1],[2], []])
    # print(graph.next(3))
    # print(graph.next_bis([0,0,1]))
    print(myHanoi.next([[3,1],[2], []]))
    # graph2 = {
    #     1: [2, 3],
    #     2: [5, 6],
    #     3: [],
    #     4: [2, 4, 6],
    #     5: [4],
    #     6: [6]
    # }
    # dico = DictGraph(graph2,[1,2])
    #
    # print(dico.getRoots())
    # print(dico.next(6))
