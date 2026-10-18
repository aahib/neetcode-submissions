class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # OR
        return len(set(nums)) != len(nums)

        # n log n solution
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
