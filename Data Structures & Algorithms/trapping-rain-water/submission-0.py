class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        maxLeft = height[left]
        maxRight = height[right]
        while left<right:
            if maxLeft<maxRight:
                left+=1
                maxLeft = max(maxLeft, height[left])
                maxWater += maxLeft-height[left]

            else:
                right-=1
                maxRight = max(maxRight, height[right])
                maxWater += maxRight - height[right]

        return maxWater




        