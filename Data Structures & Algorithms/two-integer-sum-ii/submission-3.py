class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in numbers:

            lp, rp = 0, len(numbers)-1
            while lp<rp:
                sum = numbers[lp]+numbers[rp]
                if sum < target:
                    lp+=1
                elif sum > target:
                    rp-=1
                else:
                    return [lp+1, rp+1]
