class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, j in enumerate(nums):
            if i >0 and j == nums[i-1]:
                continue

            lp = i+1 
            rp = len(nums)-1

            while lp<rp:
                sum = j + nums[lp] + nums[rp]
                if sum < 0:
                    lp+=1
                elif sum > 0:
                    rp-=1
                else:
                    result.append([j, nums[lp], nums[rp]])
                    lp+=1
                    rp-=1
                    while nums[lp] == nums[lp-1] and lp<rp:
                        lp+=1

        return result 