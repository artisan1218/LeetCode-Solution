#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
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
};

int main() {
    Solution solver;
    vector<int> coins = {2};
    int amount = 3;
    cout << solver.coinChangeDP(coins, amount) << endl;
}