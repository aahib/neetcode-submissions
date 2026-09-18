class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        eye = set()

        for i in nums:
            if i in eye:
                return True
            eye.add(i)
        return False
        