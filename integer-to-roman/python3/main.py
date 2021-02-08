class Solution:
    def multiply(self, num: str, factor: int) -> str:
        if factor == 100:
            num = num.replace("X", "M")
            num = num.replace("V", "D")
            num = num.replace("I", "C")
            return num          
        if factor == 10:
            num = num.replace("X", "C")
            num = num.replace("V", "L")
            num = num.replace("I", "X")
            return num        
    
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
            tens = self.multiply(self.intToRoman(num // 10), 10)
            return tens + self.intToRoman(num % 10)
        if num >= 100 and num <= 999:
            hundreds = self.multiply(self.intToRoman(num // 100), 100)
            return hundreds + self.intToRoman(num % 100)        
        if num >= 1000 and num <= 3999:            
            return ("M"*(num // 1000)) + self.intToRoman(num - (num // 1000)*1000)        
