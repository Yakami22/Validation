from Clean.Algorithms import loop_model_checker, predicate_model_checker_v2
from Clean.SoupRules import BehaviorSoup, BehaviorSoupSemantics


class AliceBobConfig(list):
    def __init__(self):
        list.__init__(self, [-1, -1])

    def __hash__(self):
        return self[0] + 10 * self[1]

    def __str__(self):
        """
        This method is used for our pretty printer
        """
        am, aj, bm, bj = '    ', '    ', '    ', '    '
        if self[0] == -1:
            am = '\033[1;32;40m A  \033[0m'
        elif self[0] == 0:
            aj = '\033[1;32;40mAlice\033[0m'
        else:
            am = '\033[1;32;40mA ok\033[0m'
        if self[1] == -1:
            bm = '\033[1;36;40m B  \033[0m'
        elif self[1] == 0:
            bj = '\033[1;36;40m Bob\033[0m'
        else:
            bm = '\033[1;36;40mB ok\033[0m'
        res = f"""
               /\                                                            /\\
              /  \                                                          /  \\
  ___________/ __ \____________                                 ___________/ __ \____________
 |::::::::::/ |  | \:::::::::::|                               |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|                               |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|                               |::::::::/__________\:::::::::|
 |_________|  ____  |__________|                               |_________|  ____  |__________|
  | ______ | / || \ | _______ |                                 | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||                                 ||  |   || ====== ||   |   ||
  ||--+---|| |{am}| ||---+---||        {aj}   {bj}              ||--+---|| |{bm}| ||---+---||
  ||__|___|| |   -| ||___|___||                                 ||__|___|| |   -| ||___|___||
  |========| |____| |=========|  ****************************   |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)  ----------------------------  (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,) ------------------------------ (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;; '''''''''''''''''''''''''''''' ','',,,,' /__________\,,,',',;;



"""
        return res

    def __repr__(self):
        res = self.__str__()
        return '\n' + res + '\n'


def alice_guard_def(b):
    def guard(c):
        if b == 1 and c[0] == 0:
            return False
        elif b == 0 and c[1] == 0:
            return False
        return True

    return guard


def alice_action_def(b):
    def action(c):
        if c[b] == 1:
            c[b] -= 1
        else:
            c[b] += 1

    return action


def alice_soup():
    i_conf = AliceBobConfig()
    soup_beh = BehaviorSoup(i_conf)
    for i in range(2):
        for j in range(3):
            soup_beh.add(f'{i}-{j}', alice_guard_def(i), alice_action_def(i))
    return soup_beh


def alice_is_accepted(c):
    return c[0] == 1 and c[1] == 1


def alice_in_cs(c):
    return c[0] == 0


def bob_in_cs(c):
    return c[1] == 0


def bucchi_exclusion():
    delta = {
        0: [(lambda kc: True, 0), (lambda kc: alice_in_cs(kc) and bob_in_cs(kc), 1)],
        1: [(lambda kc: True, 1)]
    }
    return 0, delta, lambda c: c == 1


if __name__ == '__main__':
    print('\n-- Predicate Model Checker --')
    soup = alice_soup()
    behavior_soup = BehaviorSoupSemantics(soup)
    trace = predicate_model_checker_v2(behavior_soup, alice_is_accepted)
    if trace:
        print(f'Trace : {trace}')
    else:
        print('No Trace.')
    print('\n-- Loops --\n')
    head, loop = loop_model_checker(behavior_soup, alice_is_accepted)
    print(f'Head : {head}\nLoop : {loop}')
