class IdentityProxy :

    def __init__(self,operand):
        self.operand = operand

    def __getattr__(self, item):
        return getattr(self.operand,item)