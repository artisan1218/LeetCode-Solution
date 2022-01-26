# Best Time to Buy and Sell Stock II problem
![image](https://user-images.githubusercontent.com/25105806/151080555-9c0cd8a0-e1ca-40ec-a6ee-855f2efd385c.png)

Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

<br />

### Approach 1: Greedy, maxProfit()
Credits to: https://www.youtube.com/watch?v=3SJ3pUkPQMc&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf

Since we are allowed to do as many transactions as we want, we can fully utilize every price difference by comparing each adjacent two days and decide whether to trade. If the price of previous day is lower than latter day, we trade. Otherwise we don't trade and check the next adjacent two days. This works because the maximum profit can be divided into many small transactions, all we need to do is to make sure each of the transaction is profitable and we don't miss out any profitable transaction.

The logic can be demonstrated by the graph:
![image](https://user-images.githubusercontent.com/25105806/151081342-924d2c78-57c9-487c-89e3-a46f96890650.png)



```python3
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/151081229-8f076cf8-5abd-4d07-9d94-66c2611353fc.png)

