from script import sum, devide


def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result


def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a, b) == result


def test_devide_prohibited():
    # запрещаем деление строк (или других нечисловых типов)
    try:
        devide("2", 4)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_devide_zero():
    a = 2
    b = 0
    try:
        devide(a, b)
        assert False, "Expected ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    test_sum()
    test_devide()
    test_devide_prohibited()
    test_devide_zero()
