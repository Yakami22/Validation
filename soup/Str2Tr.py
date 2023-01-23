from model.TransitionRelation import TransitionRelation
from soup.SemanticTransitionRelation import SemanticTransitionRelation


class Str2Tr(TransitionRelation):

    def __init__(self, operand):
        pass

    def getRoots(self):
        # return self.getRoots()
        return SemanticTransitionRelation.initialConfiguration()

    def next(self, source):
        A = SemanticTransitionRelation.enabledActions(source)
        r = []
        for a in A:
            r.append(SemanticTransitionRelation.execute(a, source))
        return r
