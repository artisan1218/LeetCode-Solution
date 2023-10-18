#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def maxProfitDP1(self, k: int, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0

        increasing_subseq = []
        record = False
        prices.append(float('-inf'))
        for i in range(len(prices)-1):
            if not record and prices[i+1] > prices[i]:
                record = True
                increasing_subseq.append(prices[i])
            elif record and prices[i+1] < prices[i]:
                record = False
                increasing_subseq.append(prices[i])
        if len(increasing_subseq) == 0:
            return 0
        
        dp = [[0] * len(increasing_subseq) for i in range(k+1)] 
        
        # dp
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                # fill in second column, first column is always 0
                if col%2==0:
                    dp[row][col] = dp[row][col-1]
                else:
                    max_p = dp[row][col-1]
                    for buy in range(0, col, 2):
                        max_p = max(max_p, increasing_subseq[col]-increasing_subseq[buy] + dp[row-1][buy])
                    dp[row][col] = max_p
        
        return dp
    
    
    def maxProfitDP2(self, prices: List[int]) -> int:
        # row of the dp table is the transaction, column is the day
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]

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
    k = 2
    prices = [4,8,6,8,7,9,4,5]
    # prices = [6,5,4,8,6,8,7,8,9,4,5]
    print(solver.maxProfitDP2(prices))






