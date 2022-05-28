#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int palindromePartitionDFSmem(string s, int k) {
        unordered_map<string, int> cache;
        return dfsMem(s, 0, k, cache);
    }

    int cost(string s, int left, int right) {
        int result = 0;
        while (left < right) {
            if (s.at(left) != s.at(right)) {
                result++;
            }
            left++;
            right--;
        }
        return result;
    }

    int dfsMem(string s, int left, int k, unordered_map<string, int>& cache) {
        // cache holds a tuple of int as key, cache[(left, k)] means the
        // min costs to make all k parts of string s[left:] palindrome
        string key = to_string(left) + "-" + to_string(k);
        if (cache.find(key) != cache.end()) {
            return cache[key];
        } else {
            if (k == 1) {
                return cost(s, left, s.size() - 1); // remaining part of s is one part, no need to split
            } else if (s.size() - left == k) {
                return 0; // every split has only one char, which is already palindrome
            } else {
                int result = INT_MAX;
                // iterate over all possible right positions
                for (int right = left + 1; right <= s.size() - k + 1; right++) {
                    int curCost = cost(s, left, right - 1); // from left to right-1 because this is the part we split
                    int nextCost = dfsMem(s, right, k - 1, cache);
                    result = min(result, curCost + nextCost);
                }
                cache[key] = result;
                return result;
            }
        }
    }

    int palindromePartitionNaive(string s, int k) {
        vector<vector<string>> result;
        vector<string> cur;
        dfs(s, k, result, cur);

        unordered_map<string, int> cache;
        int minCost = INT_MAX;
        for (auto split : result) {
            int curCost = 0;
            for (auto str : split) {
                if (cache.find(str) != cache.end()) {
                    curCost += cache[str];
                } else {
                    int value = cost(str);
                    cache[str] = value;
                    curCost += value;
                }
            }
            minCost = min(minCost, curCost);
        }
        return minCost;
    }

    int cost(string s) {
        int result = 0;
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.at(left) != s.at(right)) {
                result++;
            }
            left++;
            right--;
        }
        return result;
    }

    void dfs(string s, int k, vector<vector<string>>& result, vector<string>& cur) {
        if (cur.size() == k && s == "") {
            result.push_back(cur);
        } else {
            for (int l = 1; l <= s.length(); l++) {
                if (cur.size() < k) {
                    if (cur.size() == k - 1) {
                        cur.push_back(s);
                        dfs("", k, result, cur);
                        cur.pop_back();
                        break;
                    } else {
                        cur.push_back(s.substr(0, l));
                        dfs(s.substr(l), k, result, cur);
                        cur.pop_back();
                    }
                } else {
                    break;
                }
            }
        }
    }
};

int main() {
    string s = "aabbc";
    int k = 3;
    Solution solver;
    cout << solver.palindromePartitionNaive(s, k);
    return 0;
}