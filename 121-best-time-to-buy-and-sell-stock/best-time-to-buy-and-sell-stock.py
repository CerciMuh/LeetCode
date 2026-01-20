class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0 
        left = 0 
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[left]<prices[right]:
                maxProfit = max(maxProfit,prices[right]-prices[left])
            else:
                left=right
            right+=1
        return maxProfit
