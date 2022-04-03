#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    vector<vector<string>> result;
    vector<string> curList;

public:
    vector<vector<string>> partition(string s) {
        dfs(s, result, curList, 0);
        return result;
    }

    void dfs(string s, vector<vector<string>> &result, vector<string> &curList, int i) {
        if (i == s.length()) {
            result.push_back(curList);
        } else {
            for (int j = i; j < s.length(); j++) {
                string substr = s.substr(i, j - i + 1);
                if (isPalindrome(substr)) {
                    curList.push_back(substr);
                    dfs(s, result, curList, j + 1);
                    curList.pop_back(); // backtrack
                }
            }
        }
    }

    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution solver;
    string s = "aab";
    auto result = solver.partition(s);
    for (auto list : result) {
        for (auto substr : list) {
            cout << substr << " ";
        }
        cout << endl;
    }
    return 0;
}