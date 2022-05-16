#include <algorithm> // std::sort
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumberCountBit(vector<int>& nums) {
        int result = 0;
        for (int b = 0; b < 32; b++) {
            int sum = 0;
            for (const auto& num : nums) {
                // to see if the bth position of the 32bit int num is a 1
                // & 1 is to check if the bit is set to 1
                // we can actually skip the == 1 part, as number 1 or 0 can be used as boolean
                if (1 == ((num >> b) & 1)) {
                    sum++;
                }
            }
            sum %= 3;

            if (sum != 0) {
                result += sum << b;
            }
        }
        return result;
    }

    int singleNumberLogic(vector<int>& nums) {
        int a = 0, b = 0;
        for (int num : nums) {
            b = ~a & (b ^ num);
            a = ~b & (a ^ num);
        }
        return b;
    }
};

int main() {
    Solution solver;
    vector<int> nums = {2, 2, 2, 3, 5, 5, 5};
    cout << solver.singleNumberLogic(nums);

    return 0;
}