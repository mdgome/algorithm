# Question

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
SymbolValue
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

**Constraints:**

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

# Answer

```python
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
```
# 실행 결과
![Untitled](../../../image/leetcode/13_Roman_to_Integer/image.png)