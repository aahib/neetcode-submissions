class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Brute force approach
        # max_profit = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         current_profit = prices[j] - prices[i]
        #         if current_profit > max_profit:
        #             max_profit = current_profit
        # return max_profit 

        #One-pass
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

        # #sliding window approach
        # l = 0
        # min_price = prices[0]
        # profit = 0
        # for r in range(len(prices)):
        #     if r < prices[l]:
        #         min_price = prices[r]
        #         l = r
        #     profit = max(profit, prices[r] - min_price)
        # return profit










