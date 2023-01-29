# Palindrome Partitioning II problem
![image](https://user-images.githubusercontent.com/25105806/162550216-f6bb0d4d-1ba4-4c79-b2cd-3719985c2712.png)

Leetcode link: https://leetcode.com/problems/palindrome-partitioning-ii/

<br />

### Approach 1: Dynamic Programming, minCutOneDP()

Credit to: https://www.youtube.com/watch?v=lDYIvtBVmgo

**Note: This solution leads to TLE but it provides a good idea.**

This idea is to set up a 2d table `dp` where `dp[i][j]` stands for the min cuts needed to make `s[i:j]` a valid palindrome partitioning. Thus the final answer is located at `dp[0][n-1]` where `n` is the length of string `s`.

We must fill in the dp 2d-vector diagonally because we need to calcualte the minCut by length of the substring. So len=1, len=2, len=3, etc. Since we will cut the long substr into two short substr, we have to make sure that the minCut for short substrs are already calcualted and stored in the `dp` table, otherwise the result won't be correct.

The way we update the `dp` is as follows:
1.  If `s[i:j]` is already a palindrome, then set `dp[i][j]=0` directly.
2.  If not, then we will loop through all cutting points for the substring `s[i:j]` and calculate the min cuts using the formula: `dp[i][j] = min(dp[i][j], dp[i][cut] + dp[cut + 1][j] + 1)`, where `dp[i][cut]` is the left part of the cutting point, whose min cuts can be found in `dp` because it's shorter than the substring, same for the right part. The `+1` denotes the new cut. 

      <img src="https://user-images.githubusercontent.com/25105806/162556962-829b377d-41d4-42f5-baab-63fd686eeed4.jpg" width="50%" height="50%">
      
As shown in the image above, the longest diagonal will be calculated first (1st), then work way up and right(2nd, 3rd, etc).

<br />

```cpp
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
```

Time complexity is O(n^3) because we use `isPalindrome()` function to test whether a substring is palindrome. This is time consuming and thus lead to TLE.


<br />

### Approach 2: Dynamic Programming, minCutTwoDP()

Credit to: https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
    
The idea is to use two dynamic programming code block to fill in two key tables:
1.  `valid`: a `n`\*`n` 2d-vector storing information on whether `s[i:j]` is valid. This serves as a pre-calculated table and it can save lot of time when checking if a specific substring is a palindrome
2.  `dp`: a 1d vector. `dp[i]` means the min num of cuts for substr `s.substr(0, i)` to be a valid palindrome paritioning

<br />

`valid` will be filling by expanding the substring around the mid, each time we only check the left-most and right-most char. 
```cpp
for (int substrLen = 2; substrLen <= n; substrLen++) {
    int left = 0;
    int right = left + substrLen - 1;
    while (right < n) {
        valid[left][right] = (s[left] == s[right]) && valid[left + 1][right - 1];
        left++;
        right++;
    }
}
```


<br />

`dp` will be filling by first initialize all values to `n-1` because `n-1` is the maximum number of cuts we need to make any substring a valid palindrome partitioning. Next, we will iterate over the `dp` and:
1.  If s.substr(0, i) is already a palindrome, then we don't need to cut it. This can be done by checking `valid[0][i]`
2.  If not, then we need to cut it somewhere. We need another loop to iterate through all possible cutting point of this substring. We want to make sure that the right part of the substring after cut, is a valid palindrome. This way, we can always look up the min cuts for left part by checking `dp[cut]`. To put another word, `cut` is the cut index, we will make sure `s[cut+1:i]` is valid and we only need to consider how many cuts we need to make `s[0:cut]` valid and that is done by checking `dp[cut]`. Then simply choose the minimum cut out of ```dp[i] = min(dp[i], dp[cut] + 1)```.

```cpp
vector<int> dp(n, n - 1);
for (int i = 0; i < n; i++) {
    if (valid[0][i] == true) {
        // if s.substr(0, i) is already a palindrome, then we don't need to cut it
        dp[i] = 0;
    } else {
        for (int cut = 0; cut < i; cut++) {
            if (valid[cut + 1][i] == true) {
                dp[i] = min(dp[i], dp[cut] + 1);
            }
        }
    }
}
```

<br />

Overall, the complete code looks like this:
```cpp
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
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/162550713-e8946c18-d78c-4bb2-835c-980657fb774a.png)


<br />

### Approach 3: Dynamic Programming, minCutOddAndEvenDP()

Credits to: https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space

This solution is similar to the problem of testing if a string is a palindrome. The idea is to go through each char in the string `s` and treat each char as the center of a palindrome. Then use another loop to expand the substring until it's no longer a substring. We will expand the center in two ways:
1. Treat the substring as an odd length substring, which means the center is only on element. We only need to compare the left and right boundary, so left boundary can be written as `s[mid - r]` where `mid` the center and `r` is the radius, right boundary can be written as `s[mid + r]`. As long as the left and right are equal and we're still in the range of `s.length()`, we can update our `cut` vector using the formula `cut[mid + r] = min(cut[mid + r], cut[mid - r - 1] + 1)`. We basically cut the `s` into two parts, we will make sure the right part is always a palindrome by the loop logic, then we will get the min cuts for the left part by checking the `cut[mid - r - 1]`. The `+1` denotes the new cut. 
2. Treat the substring as an even length substring, which means the center has two elements. We still only compare the left and right boundary and expand our way out. However this time, left boundary is still `s[mid - r]`, but rigth boundary is `s[mid + r - 1]` because there are two elements in the center. Thus the update function is `cut[mid + r - 1] = min(cut[mid + r - 1], cut[mid - r - 1] + 1)`. 

Note that we need to handle an edge case where left boundary is at index 0. In this case, we will set the min cuts at right boundary(`cut[mid + r]` or `cut[mid + r + 1]`) directly to 0. This is because there is no 'left part' if the substring is at left-most index. 


```cpp
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
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/162557445-cf03a816-2ce3-4e39-b224-c57db1e9bd2b.png)

    
