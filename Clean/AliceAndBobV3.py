from Clean.Algorithms import predicate_model_checker, loop_model_checker, predicate_model_checker_v2
from Clean.Buchi import BuchiSemantics, KripkeBuchiSTR
from Clean.Models import STR2TR
from Clean.SoupRules import BehaviorSoup, BehaviorSoupSemantics


class ABConfig(list):
    def __init__(self):
        list.__init__(self, [-1, -1])

    def __hash__(self):
        return self[0] + 10 * self[1]

    def __str__(self):
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
Maison Alice {am}                   -- Maison
Maison           -- jardin {aj}{bj} -- Maison Bob {bm}
Maison                                 Maison"""

        res = f"""
    ) )        /\                                                 ) )        /\\
   =====      /  \                                               =====      /  \\
  _|___|_____/ __ \____________                                 _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|                               |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|                               |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|                               |::::::::/__________\:::::::::|
 |_________|  ____  |__________|                               |_________|  ____  |__________|
  | ______ | / || \ | _______ |                                 | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||                                 ||  |   || ====== ||   |   ||
  ||--+---|| |{am}| ||---+---||         {aj}{bj}                ||--+---|| |{bm}| ||---+---||
  ||__|___|| |   o| ||___|___||                                 ||__|___|| |   o| ||___|___||
  |========| |____| |=========| -^^-^^^^^-^^-^^^^-^^-^^^--^^^-- |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)  ,, , ,, ,,   ,,, , ,,,, ,, ,  (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)  ,, , ,, , ,, ,, ,, ,,,, ,, ,  (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;  ,, , ,, , ,, ,, ,, ,,,, ,, , ','',,,,' /__________\,,,',',;;



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
    i_conf = ABConfig()
    soup = BehaviorSoup(i_conf)
    for i in range(2):
        for j in range(3):
            soup.add(f'{i}-{j}', alice_guard_def(i), alice_action_def(i))
    return soup


def alice_is_accepted(c):
    return c[0] == 1 and c[1] == 1


def a_in_cs(c):
    return c[0] == 0


def b_in_cs(c):
    return c[1] == 0


def exclusion_buchi():
    delta = {
        0: [(lambda kc: True, 0), (lambda kc: a_in_cs(kc) and b_in_cs(kc), 1)],
        1: [(lambda kc: True, 1)]
    }
    return 0, delta, lambda c: c == 1


if __name__ == '__main__':
    print('---- Alice & Bob ----\n')

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


