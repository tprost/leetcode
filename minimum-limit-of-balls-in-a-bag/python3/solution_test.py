import pytest
import random
from solution import Solution

solution = Solution()

def test_thing():
    
    assert solution.minimumSize([1], 0) == 1
    assert solution.minimumSize([1], 1) == 1
    assert solution.minimumSize([1], 2) == 1
    assert solution.minimumSize([1], 3) == 1
    assert solution.minimumSize([2], 0) == 2
    assert solution.minimumSize([2], 1) == 1
    assert solution.minimumSize([2], 2) == 1
    assert solution.minimumSize([2], 3) == 1
    assert solution.minimumSize([3], 1) == 2
    assert solution.minimumSize([3], 2) == 1
    assert solution.minimumSize([3], 3) == 1

    assert solution.minimumSize([9], 1) == 5
    assert solution.minimumSize([9], 2) == 3

    assert solution.minimumSize([10], 2) == 4
    
    assert solution.minimumSize([1, 1], 0) == 1
    assert solution.minimumSize([1, 2], 0) == 2
    assert solution.minimumSize([1, 3], 0) == 3
    assert solution.minimumSize([2, 1], 1) == 1
    assert solution.minimumSize([2, 2], 1) == 2
    assert solution.minimumSize([2, 4, 8, 2], 4) == 2
    assert solution.minimumSize([7, 17], 2) == 7


    assert solution.minimumSize([1, 1, 1, 1, 1, 1], 6) == 1

def test_load():

    bags = []
    for i in range(0, 10**5):
        bags.append(random.randint(1, 10**5))

    assert solution.minimumSize(bags, 245) > 0

def test_load_again():

    bags = []
    operations = 0
    for i in range(1, 10**5 + 1):        
        bags.append(i)
        operations += i - 1

    assert solution.minimumSize(bags, operations) == 1
    
    
    # assert solution.minimumSize([3], 1) == 1
    # assert solution.minimumSize([9], 2) == 3    
    # assert solution.minimumSize([9], 2) == 3
