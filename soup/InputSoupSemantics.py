from soup.InputSemanticTransitionRelation import InputSemanticTransitionRelation


class InputSoupSemantics(InputSemanticTransitionRelation):
    def __init__(self, program):
        self.program = program
