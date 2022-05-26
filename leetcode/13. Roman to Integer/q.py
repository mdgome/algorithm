class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        
        temp_value = 0
        cur = 0
        while cur <(len(s)):
            if ( (cur+1) != len(s) and (s[cur] + s[cur+1] in roman_value) ) :
                temp_value = temp_value + roman_value[s[cur] + s[cur+1]]
                cur = cur +2
            else :
                temp_value = temp_value + roman_value[s[cur]]
                cur = cur +1
        return temp_value