# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return(0)
        
        profit = 0
        min_v = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] <= prices[i-1]:
                min_v = min(min_v, prices[i])
            else:
                profit = max(profit, prices[i] - min_v)
        
        return(profit)
    
    #find min to set current min
    # if not min find profit 
