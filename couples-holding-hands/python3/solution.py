from typing import List

class Solution:
    
    def isEverybodyHoldingHands(self, row: List[int]) -> bool:
        for i in range(0, len(row), 2):
            if abs(row[i] - row[i+1]) != 1:
                return False
        return True

    def isCouple(self, a: int, b:int) -> bool:
        return abs(a - b) == 1 and max(a, b) % 2 == 1

    def isGoodSwap(self, row: List[int], i: int, j: int) -> bool:
        if i % 2 == 0 and self.isCouple(row[j], row[i+1]):
            return True        
        if i % 2 == 1 and self.isCouple(row[j], row[i-1]):
            return True
        if j % 2 == 0 and self.isCouple(row[i], row[j+1]):
            return True
        if j % 2 == 1 and self.isCouple(row[i], row[j-1]):
            return True
        return False        
        
    def minSwapsCouples(self, row: List[int]) -> int:        
        if self.isEverybodyHoldingHands(row):
            return 0

        result = 100000

        for i in range(0, len(row)):
            for j in range(0, len(row)):
                # if the two seats are candidates for swapping
                if i < j and (i % 2 == 1 or i + 1 != j):

                    # if swapping the two seats puts a couple together
                    if self.isGoodSwap(row, i, j):                        
                        new = row[:]
                        new[i], new[j] = new[j], new[i]
                        result = min(result, 1 + self.minSwapsCouples(new))                      
                    
        return result



