class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in numsSet:

            if (n-1 not in numsSet): 
                streak = 0
                while (n+streak) in numsSet:
                    streak +=1

                longest = max(streak, longest)

        return longest
