from SemanticTransitionRelation import SemanticTransitionRelation
import copy


class SoupSemantics(SemanticTransitionRelation):

    def __init__(self, program) :
        self.program = program

    def initialConfiguration(self):
        return [self.program.ini] 

    def enabledActions(self, source):
        return filter ( lambda r : r.guard(source), self.program.rules)
        # pass

    def execute(self, action, source):
        # t = copy.copy(source)
        t = copy.deepcopy(source)
        return action.execute(t)

    # def rules():
    #     pass