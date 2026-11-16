from calculator import add, divide


def test_add():
    assert add(5, 3) == 8


def test_divide():
    assert divide(10, 2) == 5