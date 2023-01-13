from IdentityProxy import IdentityProxy


class ParentTraceProxy(IdentityProxy) :
    def __init__(self,operand,dict):
        self.operand = operand
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        ...
    def next(self,source):
        neighbours = self.operand.next(source)
        ...