import pytest
from main import Solution

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

@pytest.mark.parametrize("test_input,test_output",  [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (9, "IX"),
    (10, "X"),
    
])
def test_foo(test_input, test_output):
    solution = Solution()
    assert solution.intToRoman(test_input) == test_output    
