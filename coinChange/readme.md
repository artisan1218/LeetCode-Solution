# Coin Change problem
<img width="1158" alt="image" src="https://user-images.githubusercontent.com/25105806/169642926-718ebba6-867f-4a5b-9847-c3b8a91f9ba1.png">

Leetcode link: https://leetcode.com/problems/coin-change/

<br />

### Approach 1: DFS, coinChangeDFS()
The idea is to use DFS to explore all possible ways, this is the most naive way and will lead to TLE because DFS will repeatedly calculate duplicates paths. 

`dfs()` function takes `remaining` variable as the remaining amount of money we need to make up to using `coins`. 

```cpp
int coinChangeDFS(vector<int>& coins, int amount) {
    int result = -1;
    dfs(coins, amount, result, 0);
    return result;
}

void dfs(vector<int>& coins, int remaining, int& result, int cur) {
    if (remaining > 0) {
        for (const auto& coin : coins) {
            if (coin <= remaining) {
                dfs(coins, remaining - coin, result, cur + 1);
            }
        }
    } else if (remaining == 0) {
        if (cur < result || result == -1) {
            result = cur;
        }
    }
}
```

<br />

### Approach 2: DFS with memorization, coinChangeMem()
The idea is based on the approach 1 but use a different implementation to adopt memorization. 

```cpp
int coinChangeMem(vector<int>& coins, int amount) {
    unordered_map<int, int> cache;
    int result = dfsMem(coins, amount, cache);
    return result == (INT_MAX - 1) ? -1 : result;
}

int dfsMem(vector<int>& coins, int remaining, unordered_map<int, int>& cache) {
    if (remaining == 0) {
        return 0;
    } else {
        if (cache.find(remaining) != cache.end()) { // cache
            return cache[remaining];
        } else {
            int minCoins = INT_MAX - 1; // INT_MAX - 1 to avoid overflow
            for (const auto& coin : coins) {
                if (coin <= remaining) {
                    int curMin = 1 + dfsMem(coins, remaining - coin, cache);
                    minCoins = min(minCoins, curMin);
                }
            }
            cache[remaining] = minCoins; // memorization
            return cache[remaining];
        }
    }
}
```

Actual running time:\
<img width="631" alt="image" src="https://user-images.githubusercontent.com/25105806/169643679-5f0ebfb3-206f-43a8-bbaf-ccc85664e413.png">


<br />

### Approach 3: DP, coinChangeDP()
Credits to: https://www.youtube.com/watch?v=H9bfqozjoqs

We can use a 1d array `dp` to hold the minimum amount of coins needed to make up the amount. `dp[i]` stands for the minimum amount of coins needed to make up amount `i`.

The state transition function is: `dp[i] = min(dp[i], dp[i-coin] + 1)`. We need to iterate over all coins in `coins` to see the which is the minimum way.

We initialize `dp[0]` to 0 because we need 0 coins to make up the amount 0. 

```cpp
int coinChangeDP(vector<int>& coins, int amount) {
    // initialize default value of the dp array of length amount + 1 to INT_MAX
    vector<int> dp(amount + 1, INT_MAX - 1);

    dp[0] = 0; // the first value is 0 which means it takes 0 coin to make up amount 0
    for (int i = 1; i < dp.size(); i++) {
        for (const auto& coin : coins) {
            if ((i - coin) >= 0) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[dp.size() - 1] == INT_MAX - 1 ? -1 : dp[dp.size() - 1];
}
```

Time complexity is O(mn) where m is the amount and n is the length of `coins`:\
<img width="637" alt="image" src="https://user-images.githubusercontent.com/25105806/169644243-96f8c6fe-4fcf-474e-863c-4ef141ea25da.png">
