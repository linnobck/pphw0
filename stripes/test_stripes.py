from stripes import make_stripes


def test_small_horizontal():
    assert make_stripes(2, True) == [
        ["*", "*"],
        ["o", "o"],
    ]


def test_large_horizontal():
    assert make_stripes(5, True) == [
        ["*", "*", "*", "*", "*"],
        ["o", "o", "o", "o", "o"],
        ["*", "*", "*", "*", "*"],
        ["o", "o", "o", "o", "o"],
        ["*", "*", "*", "*", "*"],
    ]


def test_small_vertical():
    assert make_stripes(2, False) == [
        ["*", "o"],
        ["*", "o"],
    ]


def test_large_vertical():
    assert make_stripes(5, False) == [
        ["*", "o", "*", "o", "*"],
        ["*", "o", "*", "o", "*"],
        ["*", "o", "*", "o", "*"],
        ["*", "o", "*", "o", "*"],
        ["*", "o", "*", "o", "*"],
    ]
