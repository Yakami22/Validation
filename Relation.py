from abc import abstractmethod


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

    def getRoots(self):
        return self.roots

    def next(self, source):
        pass


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
        pass

if __name__ == '__main__':
    graph = NBits([0, 0, 0], 3)
    print(graph.next(3))
    print(graph.next_bis([0,0,1]))
