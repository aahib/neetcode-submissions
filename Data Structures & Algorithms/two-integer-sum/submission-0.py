class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preValues = {} #value:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preValues:
                return [preValues[diff], i]
            preValues[n] = i
        return
