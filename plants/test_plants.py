from plants import make_plant, FLOWER, STEM


def test_plant_flower():
    assert make_plant(1) == f" {FLOWER}\n"


def test_plant_stem_leaf():
    assert make_plant(2) == f" {FLOWER}\n~|~\n"


def test_plant_stem_only():
    assert make_plant(3) == f" {FLOWER}\n~|~\n |\n"


def test_plant_big():
    assert make_plant(8) == f" {FLOWER}\n~|~\n |\n~|~\n |\n |\n~|~\n |\n"
