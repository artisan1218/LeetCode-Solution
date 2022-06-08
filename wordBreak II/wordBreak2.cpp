#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> cur, result;
        // backtrack(s, wordDict, 0, cur, result);
        backtrack2(s, wordDict, 0, "", result);
        return result;
    }

    void backtrack(string s, vector<string>& wordDict, int i, vector<string>& cur, vector<string>& result) {
        if (i == s.length()) {
            string segStr = "";
            for (int i = 0; i < cur.size(); i++) {
                if (i != cur.size() - 1) {
                    segStr += cur[i] + " ";
                } else {
                    segStr += cur[i];
                }
            }
            result.push_back(segStr);
        } else {
            for (const auto& word : wordDict) {
                if (i + word.length() <= s.length() && s.substr(i, word.length()) == word) {
                    cur.push_back(word);
                    backtrack(s, wordDict, i + word.length(), cur, result);
                    cur.pop_back(); // backtracking
                }
            }
        }
    }

    void backtrack2(string s, vector<string>& wordDict, int i, string cur, vector<string>& result) {
        if (i == s.length()) {
            result.push_back(cur.substr(0, cur.length() - 1)); // remove the tailing space
        } else {
            for (const auto& word : wordDict) {
                if (i + word.length() <= s.length() && s.substr(i, word.length()) == word) {
                    backtrack2(s, wordDict, i + word.length(), cur + word + " ", result);
                }
            }
        }
    }
};

int main() {
    Solution solver;
    string s = "catsanddog";
    vector<string> wordDict = {"cat", "cats", "and", "sand", "dog"};
    auto result = solver.wordBreak(s, wordDict);
    for (const auto& s : result) {
        cout << s << "\n";
    }
    return 0;
}