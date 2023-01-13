from model.IdentityProxy import IdentityProxy


class ParentTraceProxy(IdentityProxy) :
    def __init__(self,operand,dict):
        super.__init__(operand)
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        ...
    def next(self,source):
        neighbours = self.operand.next(source)
        ...