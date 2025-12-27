class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        max_profit = 0

        while l < r:
            if prices[l] > prices[r]:
                l = r         
                r += 1
            elif (prices[r] - prices[l]) > max_profit:
                max_profit = prices[r] - prices[l]
                r += 1
            else:
                r += 1         

            if r >= len(prices):
                break

        return max_profit