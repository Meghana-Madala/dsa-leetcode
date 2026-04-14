class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in prices:
            if i < buy:
                profit = max(sell - buy, profit)
                buy = i
                sell = i
            elif i > sell:
                sell = i
        return max(profit, sell - buy)