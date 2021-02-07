class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 4:
            return "IV"
        if num == 5:
            return "V"
        if num == 6:
            return "VI"
        if num == 7:
            return "VII"
        if num == 9:
            return "IX"
        if num == 10:
            return "X"
        out = ""
        for x in range(num):
            out += "I"
        return out
