from earley import *


def test_hash():
    first_situation = Situation('S#', 'S', 0, 0)
    second_situation = Situation('S#', 'S', 0, 0)
    assert hash(first_situation) == hash(second_situation)


def test_eq():
    first_situation = Situation('S#', 'S', 0, 0)
    second_situation = Situation('S#', 'S', 0, 0)
    assert first_situation == second_situation


def test_add():
    a = Situation('S#', 'S', 0, 0)
    b = Situation('S#', 'S', 0, 0)

    s = set()
    s.add(a)
    s.add(b)

    assert len(s) == 1
