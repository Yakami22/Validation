from model.IdentityProxy import IdentityProxy
from model.TransitionRelation import TransitionRelation


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand : TransitionRelation, dict):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        '''
        Should return the roots of
        :return: graph roots
        parent racines sont eux meme
        '''
        neighbours = self.operand.getRoots()
        for n in neighbours:
            self.dict[n] = n
        return neighbours

    def next(self, source):
        '''
        Should return the next in graph
        :param source:
        :return: next graph
        '''
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours

    def get_trace(dic, target):
        res = [target]
        courant = target
        while courant != dic[courant]:
            courant = dic[res[-1]]
            res.append(courant)
            # print(courant.conf)
        res.reverse()
        return res
