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