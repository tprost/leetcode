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
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (11, "XI"),
    (12, "XII"),
    (13, "XIII"),
    (14, "XIV"),
    (19, "XIX"),
    (20, "XX"),
    (27, "XXVII"),
    (29, "XXIX"),
    (30, "XXX"),
    (31, "XXXI"),
    (39, "XXXIX"),
    (40, "XL"),
    (41, "XLI"),
    (49, "XLIX"),
    (50, "L"),
    (51, "LI"),
    (59, "LIX"),
    (60, "LX"),
    (61, "LXI"),
    (69, "LXIX"),
    (70, "LXX"),
    (71, "LXXI"),
    (79, "LXXIX"),
    (80, "LXXX"),
    (81, "LXXXI"),
    (89, "LXXXIX"),
    (90, "XC"),
    (91, "XCI"),
    (96, "XCVI"),
    (99, "XCIX"),
    (100, "C"),
    (101, "CI"),    
    (199, "CXCIX"),
    (200, "CC"),
    (451, "CDLI"),
    (499, "CDXCIX"),
    (500, "D"),
    (989, "CMLXXXIX"),
])
def test_foo(test_input, test_output):
    solution = Solution()
    assert solution.intToRoman(test_input) == test_output    
