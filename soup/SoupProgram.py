from soup.Rule import Rule


class SoupProgram:
    def __init__(self, ini):
        self.ini = ini
        self.rules = []

    def add(self, rule: Rule):
        self.rules.append(rule)
