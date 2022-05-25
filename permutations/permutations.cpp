#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> pre, cur;
        for (const auto& num : nums) {
            if (pre.size() == 0) {
                pre.push_back({num});
            } else {
                for (auto permutation : pre) {
                    int size = permutation.size();
                    for (int i = 0; i <= size; i++) {
                        permutation.insert(permutation.begin() + i, num);
                        cur.push_back(permutation);
                        permutation.erase(permutation.begin() + i);
                    }
                }
                pre = cur;
                cur.clear();
            }
        }
        return pre;
    }
};

int main() {
    Solution solver;
    vector<int> nums = {1, 2, 3};
    auto result = solver.permute(nums);
    for (const auto& permutation : result) {
        for (const auto& num : permutation) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}