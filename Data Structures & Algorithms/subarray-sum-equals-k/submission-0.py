class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        prefixSum = {0:1}

        for num in nums:
            curSum += num
            diff = curSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return result