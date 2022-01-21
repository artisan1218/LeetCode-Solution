# Best Time to Buy and Sell Stock problem
<img width="813" alt="image" src="https://user-images.githubusercontent.com/25105806/150488307-3b808031-4f63-4024-b2e0-b1d57bc9d7f4.png">

Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

<br />

### Approach 1: Two Pointers, maxProfitTwoPointers()
Credits to: https://www.youtube.com/watch?v=1pkOgXD63yU

The idea is to use two pointers, `buy` and `sell` to represent the day we buy in and sell, we will iterate over the `prices` array and update the buy date to be equal to sell date when sell price is lower than buy price, which means we won't be profitting, so we don't trade. But rather, move the buy date to sell date because the sell date price is lower. Move buy day to sell day is the best option to do because if there is a price in the future that is higher, we will be better off by buying at current sell day, if the there is a price in the future that is lower than current sell day, we will move current buy day to that sell day again. Then simply calculate the profit, compare it with maximum profit seen so far and update maximum profit if needed. 

```python3
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
```

Time complexity is O(n):\
<img width="734" alt="image" src="https://user-images.githubusercontent.com/25105806/150489004-37108812-a07a-43a7-8c4a-36364957d1d0.png">


<br />

### Approach 2: maxProfit2()

Credits to: https://www.youtube.com/watch?v=3RHCb8LY-X4

The idea is to iterate over the `prices` and update the lowest price seen so far, then calculate the current profit by taking the difference between current price and `minPrice`. Finally, compare and store the maximum profit.

```python3
def maxProfit2(self, prices: List[int]) -> int:
    minPrice = float('inf')
    maxProfit = 0
    for price in prices:
        minPrice = min(price, minPrice) # keeps the lowest price seen so far
        maxProfit = max(maxProfit, price-minPrice) # calculate profit between current price and min price seen so far
    return maxProfit
```

Time complexity is O(n):\
<img width="753" alt="image" src="https://user-images.githubusercontent.com/25105806/150489463-b86fd42f-64b5-4da4-b6e6-0539ec2b0bba.png">


<br />

### Approach 3: Kadane's Algorithm, maxProfitKadaneAlgorithm()
The idea is to compare the price between each two adjacent date. This works because `day3-day1 = (day2-day1) + (day3-day2)`. We will add the profit between different days to `cur_profit` and then compare it with `max_profit`. However, if the profit is negative, we simply make `cur_profit` 0, which means we don't trade as we won't make any profits. 

```python3
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
```

Time complexity is O(n):\
<img width="762" alt="image" src="https://user-images.githubusercontent.com/25105806/150490083-c72d3b98-40bb-40de-84f1-2ade4db1ffcc.png">

