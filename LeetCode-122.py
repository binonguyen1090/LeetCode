# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return(0)
    
        total = 0
        for i in range(1,len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                total += profit
        return(total)
            