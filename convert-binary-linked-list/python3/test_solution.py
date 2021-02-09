import pytest
from solution import Solution
from solution import ListNode

solution = Solution()

def test_empty():
    assert solution.getDecimalValue(None) == 0

@pytest.mark.parametrize("bits,expected", [
    ([0], 0),
    ([1], 1),
    ([1, 0], 2),
    ([1, 1], 3),
    ([1, 1, 1], 7),
    ([1, 0, 0], 4),
    ([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0], 18880),
])    
def test_one_node(bits, expected):
    head = None
    for bit in reversed(bits):        
        head = ListNode(bit, head)
    
    assert solution.getDecimalValue(head) == expected    
    
def test_one_node_with_zero():    
    head = ListNode(0, None)
    assert solution.getDecimalValue(head) == 0

def test_one_node_with_one():    
    head = ListNode(1, None)
    assert solution.getDecimalValue(head) == 1
