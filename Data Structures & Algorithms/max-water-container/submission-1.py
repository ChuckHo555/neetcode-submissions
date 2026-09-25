class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxLeft = 0
        maxRight = len(heights)-1
        maxArea = 0

        while maxLeft < maxRight:
            area = min(heights[maxLeft], heights[maxRight]) * (maxRight-maxLeft)
            maxArea = max(maxArea, area)
            if heights[maxLeft]<heights[maxRight]:
                maxLeft+=1
            else:
                maxRight-=1
        return maxArea
        