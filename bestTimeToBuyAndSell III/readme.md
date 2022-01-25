# Best Time to Buy and Sell Stock III problem
<img width="939" alt="image" src="https://user-images.githubusercontent.com/25105806/151063611-86f3d02f-83d4-4ca2-90ec-1c3e9bdce4f7.png">

Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

<br />

### Approach 1: Dynamic Programming, maxProfitDP1()
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).

Since we're only dealing with at most two transactions, we can use four variables to represent these two transactions:
* `buy1` means the profit after we buy the first stock
* `sell1` means the profit after we sell the first stock
* `buy2` means the profit after we buy the second stock
* `sell2` means the profit after we sell the second stock, which is the final answer

Next is simply go over the `prices` array and update above four variables accordingly.
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
