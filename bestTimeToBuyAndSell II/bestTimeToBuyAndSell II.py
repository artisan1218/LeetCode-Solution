# %%
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

if __name__ == '__main__':
    solver = Solution()
    prices = [7,1,5,3,6,4]
    print(solver.maxProfit(prices))

# %%



