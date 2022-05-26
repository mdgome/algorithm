# Question
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

**Note:**

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using [2's complement notation](https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in **Example 3**, the input represents the signed integer. `3`.

**Example 1:**

```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string00000000000000000000000000001011 has a total of three '1' bits.

```

**Example 2:**

```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string00000000000000000000000010000000 has a total of one '1' bit.

```

**Example 3:**

```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string11111111111111111111111111111101 has a total of thirty one '1' bits.

```

**Constraints:**

- The input must be a **binary string** of length `32`.

**Follow up:**

If this function is called many times, how would you optimize it?

# Answer
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        n(int) : 입력 숫자
        return_value(int) : 반환 값
        """
        return_value = 0

        # n의 최대 자리수는 32자리로 들어옴
        for _ in range(32):
            # 1과 bit연산 하여 True 일 경우 1 반환 
            # n = 3 일 경우 11 이며 01과 bit 연산시 1이 반환
            return_value += (n&1)
            
            # bit 연산이 완료 된 이후에 오른쪽으로 시프트 연산 진행
            # 3 = 11 bit 연산 이후 01로 변경
            n = n>>1
                
        return return_value
```

# 실행 결과
![Untitled](../../../image/leetcode/191_Number_of_1Bits/image.png)