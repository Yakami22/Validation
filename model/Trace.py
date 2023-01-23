from model.IdentityProxy import IdentityProxy


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dico):
        super().__init__(operand)
        self.dict = dico

    def roots(self):
        """
        Should return the roots of
        :return: graph roots
        parent racines sont eux meme
        """
        neighbours = self.operand.roots()
        for n in neighbours:
            self.dict[n] = n
        return neighbours

    def next(self, source):
        """
        Should return the next in graph
        :param source:
        :return: next graph
        """
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours
