from Clean.SoupRules import BehaviorSoup


class ProgramCounterConfig:
    def __init__(self):
        self.pc = 0

    def __hash__(self):
        return hash(self.pc)

    def __eq__(self, other):
        return self.pc == other.pc

    def __repr__(self) -> str:
        return str(self.pc)


def Programcounter(max):
    soup = BehaviorSoup(ProgramCounterConfig())

    def inc(c):
        c.pc = c.pc + 1

    soup.add('inc', lambda c: c.pc < max, inc)

    def reset(c):
        c.pc = 0

    soup.add('reset', lambda c: c.pc >= max, reset)

    return soup