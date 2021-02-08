class Solution:
    def prefix(self, num: int, factor: int, one: str, five: str) -> str:
        return ""        
    
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        if num >= 1 and num <= 3:
            return "I" * num
        if num == 4:
            return "IV"        
        if num >= 5 and num <= 8:
            return "V" + self.intToRoman(num-5)        
        if num == 9:
            return "IX"        
        if num >= 10 and num <= 99:
            roman = self.intToRoman(num // 10)
            roman = roman.replace("X", "C")
            roman = roman.replace("V", "L")
            roman = roman.replace("I", "X")            
            return roman + self.intToRoman(num % 10)
        if num >= 100 and num <= 999:
            roman = self.intToRoman(num // 100)
            roman = roman.replace("X", "M")
            roman = roman.replace("V", "D")
            roman = roman.replace("I", "C")            
            return roman + self.intToRoman(num % 100)
        if num >= 1000 and num <= 3999:            
            return ("M"*(num // 1000)) + self.intToRoman(num - (num // 1000)*1000)        
