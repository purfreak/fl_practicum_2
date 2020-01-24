from rule import Rule
from situation import Situation
from earley import Earley


def test_predict():
    earley = Earley('a')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'a')]
    earley.predict(0)

    is_added = False
    to_add = Situation('S', 'a', 0, 0)
    for sit in earley.situations_dict[0]:
        if sit == to_add:
            is_added = True
            break

    assert is_added


def test_scan():
    earley = Earley('a')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'a')]
    earley.situations_dict[0].add(Situation('S', 'a', 0, 0))
    earley.scan(0, 'a')

    is_added = False
    to_add = Situation('S', 'a', 0, 1)
    for sit in earley.situations_dict[1]:
        if sit == to_add:
            is_added = True
            break

    assert is_added


def test_complete():
    earley = Earley('a')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'a')]
    earley.situations_dict[0].add(Situation('S', 'a', 0, 0))
    earley.situations_dict[1].add(Situation('U', 'S', 0, 1))
    earley.complete(1)

    is_added = False
    to_add = Situation('U', 'S', 0, 1)
    for sit in earley.situations_dict[1]:
        if sit == to_add:
            is_added = True
            break

    assert is_added


def test_get_answer():
    earley = Earley('a')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'a')]
    assert earley.get_answer()

    earley = Earley('ab')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'aA'), Rule('A', 'b')]
    assert earley.get_answer()

    earley = Earley('ac')
    earley.rules_list = [Rule('U', 'S'), Rule('S', 'aA'), Rule('A', 'b')]
    assert not earley.get_answer()
