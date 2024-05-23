class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0

        selling_price=0

        buying_day=0
        selling_day=1

        while selling_day<len(prices):
            if prices[buying_day]<prices[selling_day]:
                
                selling_price=max(selling_price,(prices[selling_day]-prices[buying_day]))
                
                selling_day+=1
            else:
                
                buying_day=selling_day
                selling_day+=1
        return selling_price
            
        