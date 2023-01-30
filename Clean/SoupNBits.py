from Clean.SoupRules import soup_predicate_model_checker, BehaviorSoup


class ConfigNBits:
    def __init__(self):
        self.PC = 0

    def __hash__(self):
        return hash(self.PC)

    def __eq__(self, other):
        if not isinstance(other, ConfigNBits):
            return False
        return self.PC == other.PC

    def __repr__(self):
        return f'{self.PC}'


def create_nbits_soup(n):
    soup = BehaviorSoup(ConfigNBits())

    def flip(x):
        def action(source):
            source.PC = source.PC ^ (1 << x)
            return source
        return action
    for i in range(n):
        soup.add(f'flip {i}', lambda c: True, flip(i))

    return soup


if __name__ == '__main__':

    x = 10
    soup_predicate_model_checker(create_nbits_soup(3), lambda n: n.PC == x)

    x = 6
    soup_predicate_model_checker(create_nbits_soup(3), lambda n: n.PC == x)

    x = 1
    soup_predicate_model_checker(create_nbits_soup(3), lambda n: n.PC == x)