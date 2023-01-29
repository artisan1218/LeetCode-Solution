#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> knapsack(vector<int> weight, vector<int> value, int limit) {
        vector<vector<int>> dp(weight.size(), vector<int>(limit + 1, 0));
        for (int cap = 0; cap < limit + 1; cap++) {
            if (cap >= weight[0]) {
                dp[0][cap] = value[0];
            }
        }

        // perform dp, calculating the weights
        for (int i = 1; i < dp.size(); i++) {
            for (int curCap = 0; curCap < dp.at(i).size(); curCap++) {
                if (curCap < weight.at(i)) {
                    dp[i][curCap] = dp[i - 1][curCap];
                } else {
                    dp[i][curCap] = max(value[i] + dp[i - 1][curCap - weight[i]], dp[i - 1][curCap]);
                }
            }
        }

        // reconstruct the items based on dp
        vector<int> result;
        int i = weight.size() - 1;
        int curWt = limit;
        while (curWt != 0) {
            if (i == 0 || dp[i][curWt] != dp[i - 1][curWt]) {
                result.push_back(i);
                curWt -= weight[i];
            }
            i--;
        }

        return result;
    }
};

int main() {
    Solution solver;
    int weightLimit = 7;
    vector<int> weight = {3, 4, 5, 1};
    vector<int> value = {4, 5, 7, 1};

    auto result = solver.knapsack(weight, value, weightLimit);

    for (auto idx : result) {
        cout << idx << " ";
    }
    cout << "\n";
    return 0;
}