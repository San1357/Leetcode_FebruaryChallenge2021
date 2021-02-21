'''
Problem : Roman to Integer

#CODE :

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0 
        prev = ""
        for item in s:
            res += dict.get(item)
            if(prev+item) in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                res -= 2 *dict.get(prev)
            prev = item
        return res
    
