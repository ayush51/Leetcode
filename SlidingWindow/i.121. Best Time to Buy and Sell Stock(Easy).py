class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 #left = buy, right = sell
        maxProfit = 0
        
        while r<len(prices):
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
            else:    
                l = r
            r+=1
        return maxProfit       
    
   
