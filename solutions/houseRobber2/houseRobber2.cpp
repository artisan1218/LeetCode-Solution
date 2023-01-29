#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        } else {
            // rob second one, then we can rob the last one
            // rob first one, then cannot rob the last one
            return max(helper(nums, 1, nums.size()), helper(nums, 0, nums.size() - 1));
        }
    }

    int helper(vector<int>& nums, int start, int end) {
        int pre = 0;
        int cur = 0;
        for (int i = start; i < end; i++) {
            int tmp = pre;
            pre = cur;
            cur = max(nums.at(i) + tmp, cur);
        }
        return cur;
    }
};

int main() {
    Solution solver;
    vector<int> nums = {1, 2, 3, 1};
    cout << solver.rob(nums) << endl;
    return 0;
}