class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # buy = 0
        # sell = 1
        # while(buy < sell and sell < len(prices)):
        #     if(prices[sell] < prices[buy]):
        #         buy = sell
        #     else:
        #         max_profit = max(max_profit, prices[sell] - prices[buy])
        #     sell+=1
        # return max_profit

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