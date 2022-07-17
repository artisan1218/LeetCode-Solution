#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    // https://leetcode.com/problems/3sum-with-multiplicity/discuss/181128/10-lines-Super-Super-Easy-Java-Solution
    int threeSumMulti(vector<int>& arr, int target) {
        int result = 0;
        unordered_map<int, int> map;
        int mod = 1e9 + 7;
        for (int i = 0; i < arr.size(); i++) {
            if (map.find(target - arr[i]) != map.end()) {
                result = (result + map[target - arr[i]]) % mod;
            }

            for (int j = 0; j < i; j++) {
                int twoSum = arr[i] + arr[j];
                if (map.find(twoSum) == map.end()) {
                    map[twoSum] = 1;
                } else {
                    map[twoSum]++;
                }
            }
        }
        return result;
    }

    // https://www.youtube.com/watch?v=jZcAldZP1ag
    int threeSumMulti2(vector<int>& arr, int target) {
        int mod = 1e9 + 7;
        int result = 0;
        for (int i = 0; i < arr.size(); i++) {
            vector<int> count(101, 0); // 0 <= arr[i] <= 100
            for (int j = i + 1; j < arr.size(); j++) {
                int k = target - arr[i] - arr[j];
                if (k >= 0 && k <= 100) {
                    result = (result + count[k]) % mod;
                }
                count[arr[j]]++;
            }
        }
        return result;
    }

    // https://www.youtube.com/watch?v=jZcAldZP1ag
    int threeSumMultiMath(vector<int>& arr, int target) {
        long count[101] = {0};
        for (auto num : arr) {
            count[num]++; // count the occurrence of each number
        }

        int mod = 1e9 + 7;
        long result = 0;
        for (int i = 0; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                int k = target - i - j;
                if (k >= 0 && k <= 100) {
                    if (i == j && j == k) {
                        // Combination: from count[i] choose 3
                        result += (count[i] * (count[i] - 1) * (count[i] - 2)) / 6;
                    } else if (i == j && j != k) {
                        // Combination: from count[i] choose 2
                        result += (count[i] * (count[i] - 1) / 2) * count[k];
                    } else if (i < j && j < k) {
                        result += (count[i] * count[j] * count[k]);
                    } else {
                        continue;
                    }
                }
            }
        }
        return result % mod;
    }
};

int main() {
    vector<int> arr = {1, 1, 2, 2, 2, 2};
    Solution solver;
    int result = solver.threeSumMultiMath(arr, 5);
    cout << result << endl;
}