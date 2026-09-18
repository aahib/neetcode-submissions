class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0

        for num in nums:
            #checking if num - 1 exists in set
            if num-1 not in nums_set:
                streak = 1
                current = num
            #streack logic
                while(current + 1 in nums_set):
                    streak += 1
                    current += 1
                 #keeping largest streak
                length = max(streak, length)
        return length