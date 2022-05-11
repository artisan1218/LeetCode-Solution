#include <algorithm> // std::sort
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumberCount(vector<int>& nums) {
        unordered_map<int, int> map;
        for (const auto& num : nums) {
            if (map.find(num) != map.end()) {
                map[num]++;
            } else {
                map[num] = 1;
            }
        }
        for (const auto& pair : map) {
            if (pair.second == 1) {
                return pair.first;
            }
        }
        return -1;
    }

    int singleNumberSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i = i + 2) {
            if (nums.at(i) != nums.at(i - 1)) {
                return nums.at(i - 1);
            }
        }
        return nums.at(nums.size() - 1);
    }

    int singleNumberBit(vector<int>& nums) {
        int result = 0;
        for (const auto& num : nums) {
            result = result ^ num;
        }
        return result;
    }
};

int main() {
    Solution solver;
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << solver.singleNumberBit(nums);
    return 0;
}