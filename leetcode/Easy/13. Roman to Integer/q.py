class Solution:
    def romanToInt(self, s: str) -> int:
        """
        roman_value (int) : 로마자 텍스트 비교를 위한 dict
        s (str) : 문자
        return_value(int) : 비교 완료된 문자열을 숫자로 변환하여 저장 및 반환 변수
        """
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
        
        return_value = 0
        cur = 0
        while cur <(len(s)):
            # IV, IX, XL, XC, CD, CM 이 s에 있을 경우 비교
            if ( (cur+1) != len(s) and (s[cur] + s[cur+1] in roman_value) ) :
                # roman_value[s[cur] + s[cur+1]] # IV, IX, XL, XC, CD, CM 중 맞는 숫자 반환
                return_value = return_value + roman_value[s[cur] + s[cur+1]]
                # 2개의 문자열을 비교하므로 cur = cur + 2
                cur = cur +2
            else :
                # I, V, X, L, C, D, M 중 맞는 숫자 반환
                return_value = return_value + roman_value[s[cur]]
                # 1개의 문자열만 비교하였으므로 cur = cur + 1
                cur = cur +1
        return return_value