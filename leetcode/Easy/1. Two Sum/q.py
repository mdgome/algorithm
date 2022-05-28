class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for index, value in enumerate(nums):
            if target - value in checker:
                return [checker[target - value], index]
            else:    
                checker[value] = index