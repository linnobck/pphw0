from palindromes import find_palindromes


def test_palindromes_none():
    assert find_palindromes([]) == []


def test_palindromes_no_matches():
    assert find_palindromes(["hi", "there"]) == []


def test_palindromes_one_matches():
    assert find_palindromes(["hi", "mom"]) == ["mom"]


def test_palindromes_longer_match():
    assert find_palindromes(["red", "racecar"]) == ["racecar"]


def test_palindromes_repeat_matches():
    assert find_palindromes(["wow", "mom", "wow"]) == ["mom", "wow"]


def test_palindromes_alpha_sort():
    assert find_palindromes(["zaz", "yo", "pop", "mom", "racecar", "abc", "dad"]) == [
        "dad",
        "mom",
        "pop",
        "racecar",
        "zaz",
    ]
