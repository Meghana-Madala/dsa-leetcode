class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n=len(prices)
        # curr_buy=prices[0]
        # max_profit=0
        # for i in range(1,n):
        #     if prices[i]<curr_buy:
        #         curr_buy=prices[i]
        #     else:
        #         max_profit=max(prices[i]-curr_buy, max_profit)
        # return max_profit
        max_profit = 0
        buy = 0
        sell = 1
        while(buy < sell and sell < len(prices)):
            if(prices[sell] < prices[buy]):
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            sell+=1
        return max_profit