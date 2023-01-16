class Rule:
        def __init__(self, name, guard , action):
            self.name = name 
            self.guard = guard
            self.action = action

        def execute(self, config):
            return