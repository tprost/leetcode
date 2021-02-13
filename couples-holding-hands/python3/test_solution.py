import pytest
from solution import Solution

solution = Solution()
@pytest.mark.parametrize("seats,expected_swaps", [
    ([], 0),
    ([0, 1, 2, 3], 0),
    ([1, 0, 2, 3], 0),
    ([0, 1, 3, 2], 0),
    ([0, 1, 3, 2], 0),
    ([0, 1, 2, 3], 0),
    ([1, 2, 0, 3], 1),
    ([3, 2, 1, 0], 0),
    ([5, 4, 3, 2, 1, 0], 0),
    ([5, 3, 4, 2, 1, 0], 1),
    ([5, 4, 2, 1, 0, 3], 1),
    ([1, 2, 3, 4, 5, 0], 2),
    ([2, 1, 3, 4, 5, 0], 2),
    ([5, 1, 2, 4, 3, 0], 2),
    ([0, 5, 1, 3, 4, 2], 2),
    ([6, 0, 7, 5, 1, 3, 4, 2], 3),
    ([0, 1, 2, 3, 4, 6, 5, 7], 1),
    ([0, 1, 7, 4, 3, 2, 5, 6], 1),
    ([6, 1, 7, 4, 3, 2, 5, 0], 2),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ([1, 2, 3, 4, 5, 6, 7, 0], 3),
    ([0, 16, 2, 17, 4, 18, 6, 20, 1, 3, 5, 7, 9, 11, 13, 15, 8, 21, 10, 19, 12, 22, 14, 23], 5),
])
def test_min_swaps_couples(seats, expected_swaps):
    assert solution.minSwapsCouples(seats) == expected_swaps

def test_sixty():
    seats = list(range(1, 60))
    seats.append(0)
    assert solution.minSwapsCouples(seats) == 29    

