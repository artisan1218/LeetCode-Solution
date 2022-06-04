#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool wordBreakDP1(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet;
        for (auto word : wordDict) {
            wordSet.insert(word);
        }

        vector<bool> dp(s.length(), false);
        // validIdxList stores the indices of all valid substring so far
        // so that we don't have to iterate over all elements in dp but only valid(true) index
        vector<int> validIdxList;
        for (int i = 0; i < s.length(); i++) {
            if (wordSet.find(s.substr(0, i + 1)) != wordSet.end()) {
                dp[i] = true;
                validIdxList.push_back(i);
            } else {
                // only look into valid position
                for (auto validIdx : validIdxList) {
                    if (wordSet.find(s.substr(validIdx + 1, i - validIdx)) != wordSet.end()) {
                        dp[i] = true;
                        validIdxList.push_back(i);
                        break;
                    }
                }
            }
        }

        return dp[dp.size() - 1];
    }

    // https://www.youtube.com/watch?v=Sx9NNgInc3A
    bool wordBreakDP2(string s, vector<string>& wordDict) {
        vector<bool> dp(s.length() + 1, false);
        dp[s.length()] = true;

        for (int i = s.length() - 1; i >= 0; i--) {
            for (const auto& word : wordDict) {
                if (i + word.length() <= s.length() && s.substr(i, word.length()) == word) {
                    dp[i] = dp[i + word.length()];
                    if (dp[i] == true) {
                        break;
                    }
                }
            }
        }
        return dp[0];
    }
};

int main() {
    string s = "leetcode";
    vector<string> wordDict = {"leet", "code", "lee"};
    Solution solver;
    cout << solver.wordBreakDP2(s, wordDict);
    return 0;
}