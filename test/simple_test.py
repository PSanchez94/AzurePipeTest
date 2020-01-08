from simple_defs import simple_sum


def test_simplesum():
    assert simple_sum(1, 1) == 2


def test_failingsum():
    assert not simple_sum(1, 1) == 3
