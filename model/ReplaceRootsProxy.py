from model.IdentityProxy import IdentityProxy


class ReplaceRootsProxy(IdentityProxy):
    def __init__(self, operand, newRoots):
        super.__init__(operand)
        self.newRoots = newRoots

    def roots(self):
        return self.newRoots
