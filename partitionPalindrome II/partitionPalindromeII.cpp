#include <iostream>
#include <vector>
using namespace std;

class Solution {

public:
    // https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
    int minCutTwoDP(string s) {
        int n = s.length();
        // a n by n 2d-vector storing information on whether s[i:j] is valid
        vector<vector<int>> valid(n, vector<int>(n, true));

        // fill in the 2d-vector in a dp way. We will expand the substring around
        // the mid, each time we only check the left-most and right-most char
        for (int substrLen = 2; substrLen <= n; substrLen++) {
            int left = 0;
            int right = left + substrLen - 1;
            while (right < n) {
                valid[left][right] = (s[left] == s[right]) && valid[left + 1][right - 1];
                left++;
                right++;
            }
        }

        // minCut dp. dp[i] means the minCut of substr s.substr(0, i)
        // Initialized all elements to n-1, which is the max number of cut possible
        vector<int> dp(n, n - 1);
        for (int i = 0; i < n; i++) {
            if (valid[0][i] == true) {
                // if s.substr(0, i) is already a palindrome, then we don't need to cut it
                dp[i] = 0;
            } else {
                // cut is the cut index, we will make sure s[cut+1:i] is valid and
                // we only need to consider how many cuts we need to make s[0:cut] valid
                // and that is done by checking dp[cut]
                for (int cut = 0; cut < i; cut++) {
                    if (valid[cut + 1][i] == true) {
                        dp[i] = min(dp[i], dp[cut] + 1);
                    }
                }
            }
        }

        return dp[n - 1];
    }

    // https://www.youtube.com/watch?v=lDYIvtBVmgo
    int minCutOneDP(string s) {
        int n = s.length();
        // initialize a 2d-vector where dp[i][j] stands for the min cut needed to
        // make s[i:j] a palindrome
        vector<vector<int>> dp(n, vector<int>(n, n - 1));

        // we must fill in the dp 2d-vector diagonally because we need to
        // calcualte the minCut by length of the substring
        // so len=1, len=2, len=3, etc. Since we will cut the long substr into two short substr,
        // we have to make sure that the minCut for short substrs are already calcualted and stored
        // in the dp table, otherwise the result won't be correct
        for (int substrLen = 1; substrLen <= n; substrLen++) {
            int l = 0;
            int r = l + substrLen - 1;
            while (r < n) {
                if (isPalindrome(s.substr(l, substrLen))) {
                    dp[l][r] = 0;
                } else {
                    for (int cut = l; cut < r; cut++) {
                        // split the substr into two parts
                        // and get the minCut of each part separately by looking up dp table
                        dp[l][r] = min(dp[l][r], dp[l][cut] + dp[cut + 1][r] + 1);
                    }
                }
                l++;
                r++;
            }
        }

        return dp[0][n - 1];
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

    // https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.
    int minCutOddAndEvenDP(string s) {
        int n = s.length();
        vector<int> cut(n, 0);
        for (int i = 0; i < n; i++)
            cut[i] = i;

        for (int mid = 1; mid < n; mid++) {
            // expand around mid to check if substring is palindrome
            // odd length substr
            for (int r = 0; mid - r >= 0 && mid + r < n && s[mid - r] == s[mid + r]; r++) {
                // mid - r is the left boundary of the substr and mid + r is the right boundary
                if (mid - r == 0) {
                    cut[mid + r] = 0;
                } else {
                    // cut[mid - r - 1] is the minCut that makes s[0:mid-r-1] palindrome
                    cut[mid + r] = min(cut[mid + r], cut[mid - r - 1] + 1);
                }
            }

            // even length substr, center is the middle two chars. mid is the right one
            // that's why left boundary char is mid-r+1 and right boundary char is mid+r
            for (int r = 1; mid - r >= 0 && mid + r - 1 < n && s[mid - r] == s[mid + r - 1]; r++) {
                if (mid - r == 0) {
                    cut[mid + r - 1] = 0;
                } else {
                    cut[mid + r - 1] = min(cut[mid + r - 1], cut[mid - r - 1] + 1);
                }
            }
        }

        return cut[n - 1];
    }
};

int main() {
    Solution solver;
    string s = "aab";
    int minLen = solver.minCutOddAndEvenDP(s);
    cout << minLen << endl;

    return 0;
}