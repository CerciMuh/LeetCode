class Solution:
    def maxArea(self, height: List[int]) -> int:
            absoluteMax = 0
        

            currentMax = 0
            l = 0
            r = len(height)-1
            while (l<r):
                currentMax = min(height[l],height[r]) * ((r+1)-(l+1))
                if (currentMax > absoluteMax):
                    absoluteMax = currentMax
                if height[l] < height[r]:
                    l += 1
                else:
                    r -= 1   
            return absoluteMax            