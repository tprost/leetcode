from typing import List

buttons = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
#
# Iterate through possible combinations using a "combination lock"
# style array of indexes that we iterate through algorithmically.
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        phone_numbers = []

        combo = []
        for i in range(0, len(digits)):
            combo.append(0)            

        done = False

        while not done:

            phone_number = ""
            for i in range(0, len(combo)):
                phone_number += buttons[digits[i]][combo[i]]
            phone_numbers.append(phone_number)
            
            for i in range(len(digits) - 1, -1, -1):
                if combo[i] < len(buttons[digits[i]]) - 1:
                    combo[i] = combo[i] + 1
                    break
                else:
                    combo[i] = 0
                if combo[i] == 0 and i == 0:
                    done = True            
                

        return phone_numbers
