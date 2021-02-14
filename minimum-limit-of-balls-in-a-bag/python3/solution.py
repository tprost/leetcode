from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:        
        if maxOperations == 0:
            return max(nums)

        # range of possible minimum sizes to try
        window = [1, max(nums) + 1]
        
        best = max(nums)
        while window[0] < window[1]:
            # candidate minimum
            i = (window[0] + window[1]) // 2
            count = 0
            for num in sorted(nums, reverse=True):
                if num > i:
                    if num % i == 0:
                        count += (num // i) - 1
                    else:
                        count += num // i
                if count > maxOperations:
                    break
            if count <= maxOperations:
                best = min(best, i)
                if window[1] >= i:
                    window[1] = i                    
            else:
                if window[0] <= i:
                    window[0] = i + 1
                
        return best
        
