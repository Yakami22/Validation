from model.TransitionRelation import TransitionRelation

class Str2Tr(TransitionRelation):
    def getRoots(self):
        return super().getRoots()
        # str.initalConfiguration()

    def next(self, source):
        return super().next(source)
