# Best Time to Buy and Sell Stock IV problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/18593c50-2f8a-45b6-a1ee-83ff9812d1a0)


Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

<br />

### Approach 1: Dynamic Programming, maxProfitDP1()
Some observations:

1. If we plot the prices on the plane, we can see that we only need to care about the prices at the start and end of an increasing sub-sequences. Because for those prices within an increasing sequences, we are better off not selling them as the price will go up. For example `6 5 4 8 6 8 7 8 9 4 5` becomes `4 8 6 8 7 9 4 5`, because `6 5` is a decreasing sub-sequence and we shouldn't do anything, and `8` is in an increasing sub-sequence, if we buy in, we should buy before `8` because `7` is lower and if we sell, we should sell after `8`, because `9` is higher, so `8` can be skipped.
2. The dp matrix at `[i][j]` means the max profit we can get from prices list up to `j` given we can have max `i` operations
3. The max profit at `[i][j]` is the max between yesterday's profit(`dp[row][col-1]`) and the max profit of buy at a previous day and sell today, which can be found in a loop(`increasing_subseq[col]-increasing_subseq[buy] + dp[row-1][buy]`)

This solution is slow because of #3, where we find the max profit in another loop. 

```python3
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
        
        return dp[-1][-1]
```

Time complexity is O(n^2*k):\
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/282143b9-5448-4b53-8cff-bd47e7070abe)



<br />

### Approach 2: Dynamic Programming, maxProfitDP2()
The second solution is a generalized case of [Best Time To Buy And Sell III](https://github.com/artisan1218/LeetCode-Solution/tree/main/solutions/bestTimeToBuyAndSell%20III#approach-3-dynamic-programming-maxprofitdp3)



