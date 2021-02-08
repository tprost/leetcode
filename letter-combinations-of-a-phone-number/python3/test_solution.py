import pytest
from solution import Solution

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_solution():
    solution = Solution()
    assert solution.letterCombinations("") == []
    
@pytest.mark.parametrize("phone_number,combinations",  [
    ("2", ["a", "b", "c"]),
    ("3", ["d", "e", "f"]),
    ("4", ["g", "h", "i"]),
    ("5", ["j", "k", "l"]),
    ("6", ["m", "n", "o"]),
    ("7", ["p", "q", "r", "s"]),
    ("8", ["t", "u", "v"]),
    ("9", ["w", "x", "y", "z"]),
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
])
def test_combinations(phone_number, combinations):
    solution = Solution()
    assert solution.letterCombinations(phone_number) == combinations

def test_solution_3():
    solution = Solution()
    assert len(solution.letterCombinations("2345")) == 81

# def test_solution_4():
#     solution = Solution()
#     assert solution.letterCombinations("32") == ["da","db","dc","ea","eb","ec","fa","fb","fc"]
