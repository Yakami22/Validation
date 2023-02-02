from Clean.SoupRules import BehaviorSoup, soup_predicate_model_checker, BehaviorSoupSemantics


class ConfigurationAliceBob:

    def __init__(self):
        self.aliceFlag = 0
        self.bobFlag = 0

    def __hash__(self):
        return int(hash(self.aliceFlag + self.bobFlag))

    def __eq__(self, other):
        return self.aliceFlag == other.aliceFlag & self.bobFlag == other.bobFlag

    def __repr__(self):
        return str(self.aliceFlag) + str(self.bobFlag)


def AliceAndBob():
    soup = BehaviorSoup(ConfigurationAliceBob())

    def AliceToCriticalSection(c):
        c.aliceFlag = 1

    soup.add("AliceToCriticalSection", lambda c: c.aliceFlag == 0, AliceToCriticalSection)

    def BobToCriticalSection(c):
        c.bobFlag = 1

    soup.add("BobToCriticalSection", lambda c: c.bobFlag == 0, BobToCriticalSection)

    def AliceToInitial(c):
        c.aliceFlag = 0

    soup.add("AliceToInitial", lambda c: c.aliceFlag == 1, AliceToInitial)

    def BobToInitial(c):
        c.bobFlag = 0

    soup.add("BobToInitial", lambda c: c.bobFlag == 1, BobToInitial)

    return soup


if __name__ == '__main__':
    program = AliceAndBob()

    soup_predicate_model_checker(program, lambda c: c.bobFlag == 0)

    print("deadlock: ")
    soup_predicate_model_checker(program, lambda c: len(BehaviorSoupSemantics(program).actions(c)) == 0)

    print("Critical Section: ")
    soup_predicate_model_checker(program, lambda c: c.aliceFlag == 1 and c.bobFlag == 1)
