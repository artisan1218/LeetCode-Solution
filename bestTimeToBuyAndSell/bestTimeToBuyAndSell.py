#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List

class Solution:
    # https://www.youtube.com/watch?v=1pkOgXD63yU
    def maxProfitTwoPointers(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            # since buy price is higher than sell price, we should move the buy day to sell day in order to profit
            if prices[buy] > prices[sell]:
                # move buy day to sell day is the best option to do because if there is a price in the future
                # that is higher, we will be better off by buying at current sell day.
                # if the there is a price in the future that is lower than current sell day,
                # we will move current buy day to that sell day again.
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
            sell += 1
        return maxProfit

    # https://www.youtube.com/watch?v=3RHCb8LY-X4
    def maxProfit2(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(price, minPrice) # keeps the lowest price seen so far
            maxProfit = max(maxProfit, price-minPrice) # calculate profit between current price and min price seen so far
        return maxProfit

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/263197/Python-2-solutions%3A-Min-So-Far-Kadane's-Algorithm-with-Picture-O(1)-in-Space
    def maxProfitKadaneAlgorithm(self, prices: List[int]) -> int:
        cur_profit = 0
        max_profit = 0
        for i in range(len(prices)-1):
            # calculate the profit between two adjacent days and add the profit to cur_profit
            # only calculate the price difference between two adjacent days because day3-day1 = (day2-day1) + (day3-day2)
            cur_profit += prices[i+1] - prices[i]
            # always keep profit positive, which means we don't trade if sell price is lower than buy price
            cur_profit = max(cur_profit, 0)
            max_profit = max(max_profit, cur_profit)
        return max_profit

if __name__ == '__main__':
    solver = Solution()
    prices = [7,1,5,3,6,4]
    result = solver.maxProfitTwoPointers(prices)
    print(result)


# In[ ]:




