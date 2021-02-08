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
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        
        if digits in buttons:
            return buttons[digits]
        
        phone_numbers = []        
        tails = self.letterCombinations(digits[1:])
        for letter in buttons[digits[0]]:
            for tail in tails:
                phone_numbers.append(letter + tail)
        return phone_numbers
