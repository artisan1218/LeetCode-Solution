# Best Time to Buy and Sell Stock IV problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/18593c50-2f8a-45b6-a1ee-83ff9812d1a0)


Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

<br />

### Approach 1: Dynamic Programming, maxProfitDP1()
Some observations:

1. If we plot the prices on the plane, we can see that we only need to care about the prices at the start and end of an increasing sub-sequences. Because for those prices within an increasing sequences, we are better off not selling them as the price will go up. For example `6 5 4 8 6 8 7 8 9 4 5` becomes `4 8 6 8 7 9 4 5`, because `6 5` is a decreasing sub-sequence and we shouldn't do anything, and `8` is in an increasing sub-sequence, if we buy in, we should buy before `8` because `7` is lower and if we sell, we should sell after `8`, because `9` is higher, so `8` can be skipped.
2. The dp matrix at `[i][j]` means the max profit we can get from prices list up to `j` given we can have max `i` operations
3. The max profit at `[i][j]` is the max between yesterday's profit(`dp[row][col-1]`) and 


```python3
def maxProfitDP1(self, prices: List[int]) -> int:
    buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
    for p in prices:
        # we want to maximize the profit, so we take max
        buy1 = max(buy1, -p) # we buy the first stock, which means the profit is negative
        sell1 = max(sell1, buy1 + p) # sell the first stock, simply add the sell price to buy1
        buy2 = max(buy2, sell1 - p) # buy the second stock, so deduct the price from the first sell profit
        sell2 = max(sell2, buy2 + p) # sell the second stock, add the sell price to buy2
    return sell2
```

Time complexity is O(n):\
<img width="791" alt="image" src="https://user-images.githubusercontent.com/25105806/151064386-454f0848-83a8-4151-bde9-d7572ef6b1ce.png">


<br />

### Approach 2: Dynamic Programming, maxProfitDP2()
The second solution is similar to the first one, but we use cost instead of profit when updating all four variables:
* `buy1` means the price we pay to buy the first stock, **NOT** the profit
* `sell1` means the profit we can make by selling the first stock at price `p`
* `buy2` means the price we pay to buy the second stock. This price should be `p-sell1` because `sell1` is the profit of the first trade, which means our cost for second stock is not price `p` but `p`-'profit'
* `sell2` means the profit we can make by selling the second stock at price `p`

```python3
def maxProfitDP2(self, prices: List[int]) -> int:
    buy1, sell1, buy2, sell2 = float('inf'), 0, float('inf'), 0
    for p in prices:
        buy1 = min(buy1, p) # minimize the buy-in price
        sell1 = max(sell1, p-buy1) # maximize the profit of first sell
        buy2 = min(buy2, p-sell1) # minimize the price, since we've already made profit of sell1, the buy-in price should be p-sell1
        sell2 = max(sell2, p-buy2) # calculate profit
    return sell2
```

Time complexity is O(n):\
<img width="797" alt="image" src="https://user-images.githubusercontent.com/25105806/151064938-f996f9f0-f255-4c3b-9315-09c746a2ae99.png">


