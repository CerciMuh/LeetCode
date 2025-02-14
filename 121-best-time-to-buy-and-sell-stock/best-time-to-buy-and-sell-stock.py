class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy= 0  # index
        sell=0
        maximumProfit = 0
        for i in range(len(prices)):
            maximumProfit = max(maximumProfit, prices[i] - prices[buy])
            if prices[i] < prices[buy]:
                buy = i
            sell +=1 # redundtn
        if maximumProfit<=0:
            return 0 
        return maximumProfit        

        