# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def getLength(self, head: ListNode) -> int:
        if head == None:
            return 0
        if head.next == None:
            return 1
        return 1 + self.getLength(head.next)
    
    def getDecimalValue(self, head: ListNode) -> int:
        if head == None:
            return 0
        if head.next:        
            val = head.val * 2 ** ( self.getLength(head) - 1)
            val += self.getDecimalValue(head.next)            
            return val        
        return head.val
