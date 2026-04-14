class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        curr_buy=prices[0]
        max_profit=0
        for i in range(1,n):
            if prices[i]<curr_buy:
                curr_buy=prices[i]
            else:
                max_profit=max(prices[i]-curr_buy, max_profit)
        return max_profit
        