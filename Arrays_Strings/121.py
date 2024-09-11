class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        minprice = float('inf')

        for price in prices :
            if price<minprice:
                minprice = price
            
            profit = price-minprice  
            if(profit>maxprofit):
                maxprofit = profit
        return maxprofit          


