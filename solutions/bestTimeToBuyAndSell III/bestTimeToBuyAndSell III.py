#!/usr/bin/env python
# coding: utf-8

# In[14]:


from typing import List

class Solution:
    def maxProfitDP1(self, prices: List[int]) -> int:
        # buy1 means the profit after we buy the first stock
        # sell1 means the profit after we sell the first stock
        # buy2 means the profit after we buy the second stock
        # sell2 means the profit after we sell the second stock, which is the final answer
        buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
        for p in prices:
            # we want to maximize the profit, so we take max
            buy1 = max(buy1, -p) # we buy the first stock, which means the profit is negative
            sell1 = max(sell1, buy1 + p) # sell the first stock, simply add the sell price to buy1
            buy2 = max(buy2, sell1 - p) # buy the second stock, so deduct the price based on first sell profit
            sell2 = max(sell2, buy2 + p) # sell the second stock, add the sell price to buy2
        return sell2

    def maxProfitDP2(self, prices: List[int]) -> int:
        # buy1 means the price we pay to buy the first stock, NOT the profit
        # sell1 means the profit we can make by selling the first stock at price p
        # buy2 means the price we pay to buy the second stock. This price should be p-sell1 because sell1 is the profit of the first trade
        # which means our cost for second stock is not price p but p-profit
        # sell2 means the profit we can make by selling the second stock at price p
        buy1, sell1, buy2, sell2 = float('inf'), 0, float('inf'), 0
        for p in prices:
            buy1 = min(buy1, p) # minimize the buy-in price
            sell1 = max(sell1, p-buy1) # maximize the profit of first sell
            buy2 = min(buy2, p-sell1) # minimize the price, since we've already made profit of sell1, the buy-in price should be p-sell1
            sell2 = max(sell2, p-buy2) # calculate profit
        return sell2

    # this solution generalize to k transactions
    # credits to https://www.youtube.com/watch?v=oDhu5uGq_ic&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf
    def maxProfitDP3(self, prices: List[int]) -> int:
        numTransaction = 2 # number of transactions
        # row of the dp table is the transaction, column is the day
        dp = [[0 for _ in range(len(prices))] for _ in range(numTransaction+1)]

        # row 0 and column 0 is all 0 because doing 0 transaction or only 1 day cannot generate any profits
        # start at day 2 and transaction 1
        for transaction in range(1, len(dp)):
            minCost = prices[0]
            for day in range(1, len(dp[transaction])):
                prevProfit = dp[transaction][day-1] # the profit won't change if we do nothing
                currProfit = prices[day]-minCost # minimum cost since previous transaction
                dp[transaction][day] = max(prevProfit, currProfit)
                # because we're computing the cost since previous transaction, we should look at the previous row
                minCost = min(minCost, prices[day]-dp[transaction-1][day])
        return dp[-1][-1]



if __name__ == '__main__':
    solver = Solution()
    prices = [1, 4, 2, 5, 0, 5] #[3,3,5,0,0,3,1,4] 
    print(solver.maxProfitDP3(prices))

