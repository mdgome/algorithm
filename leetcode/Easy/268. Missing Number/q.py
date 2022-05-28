class Solution:
    def missingNumber(self, nums: List[int]) -> int:
				# 숫자가 들어오며, n(n+1)/2 의 몫과 nums의 전체 합을 빼면 1개의 빠진 숫자를 구할 수 있다.
        return ((len(nums) * (len(nums)+1)) // 2 ) - sum(nums)