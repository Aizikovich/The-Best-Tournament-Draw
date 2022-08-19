from random import shuffle

dereg_a = ['Asaf', 'Tomer', 'Roi', 'Amit', 'Dar', 'Paz', 'Barak']
dereg_b = ['Eran', 'Omri', 'Yoav', 'Matan', 'Dino', 'Guy', 'Dor']

names = dereg_a + dereg_b

allowed = [
    ('Asaf', 'Eran'), ('Asaf', 'Omri'), ('Asaf', 'Yoav'), ('Asaf', 'Matan'), ('Asaf', 'Dino'), ('Asaf', 'Guy'),
    ('Tomer', 'Eran'), ('Tomer', 'Yoav'), ('Tomer', 'Matan'), ('Tomer', 'Dino'), ('Tomer', 'Guy'), ('Tomer', 'Dor'),
    ('Roi', 'Eran'), ('Roi', 'Omri'), ('Roi', 'Yoav'), ('Roi', 'Dino'), ('Roi', 'Guy'), ('Roi', 'Dor'),
    ('Amit', 'Eran'), ('Amit', 'Omri'), ('Amit', 'Yoav'), ('Amit', 'Matan'), ('Amit', 'Guy'), ('Amit', 'Dor'),
    ('Dar', 'Eran'), ('Dar', 'Omri'), ('Dar', 'Yoav'), ('Dar', 'Matan'), ('Dar', 'Dino'), ('Dar', 'Guy'),
    ('Paz', 'Omri'), ('Paz', 'Yoav'), ('Paz', 'Matan'), ('Paz', 'Dino'), ('Paz', 'Guy'), ('Paz', 'Dor'),
    ('Barak', 'Eran'), ('Barak', 'Omri'), ('Barak', 'Matan'), ('Barak', 'Dino'), ('Barak', 'Guy'), ('Barak', 'Dor')
]


def clean_options(lst: list, pair: tuple) -> list:
    """
    clean all pairs that choose by the recursion
    """
    new_options = []
    x, y = pair
    for couple in lst:
        if not (x == couple[0] or y == couple[1]):
            new_options.append(couple)
    return new_options


def choose_teams_rec(options: list, res: list) -> list:

    # Base cases
    if len(res) > 7:
        return []
    if len(options) == 0:
        if len(res) == 7:
            return res
        return []

    # Recursive step
    choose = choose_teams_rec(clean_options(options, options[0]), res + [options[0]])
    not_choose = choose_teams_rec(options[1:], res)
    if choose:
        return choose
    if not_choose:
        return not_choose


def choose_teams(options: list) -> list:
    """
    Wrapper function for the recursive choose
    """
    teams = []
    shuffle(options)
    draw = choose_teams_rec(options, [])
    for couple in draw:
        x, y = couple
        teams.append(f"{x} & {y}\n")
    return teams

