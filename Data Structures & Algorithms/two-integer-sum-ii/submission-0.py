class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, j in enumerate(numbers):
            diff = target - j
            if diff in hashMap:
                return [hashMap[diff] +1, i + 1]
            hashMap[j] = i