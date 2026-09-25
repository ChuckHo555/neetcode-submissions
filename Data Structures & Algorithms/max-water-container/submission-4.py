class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights)-1
        finalArea = 0

        while lp<rp:
            maxHeight = min(heights[lp], heights[rp])
            maxLength = rp - lp 
            currentArea = maxHeight * maxLength
            finalArea = max(finalArea, currentArea)
            if heights[lp]<heights[rp]:
                lp+=1
            elif heights[rp]<heights[lp]:
                rp-=1
            else:
                lp+=1

        return finalArea
