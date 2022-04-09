# Palindrome Partitioning II problem
![image](https://user-images.githubusercontent.com/25105806/162550216-f6bb0d4d-1ba4-4c79-b2cd-3719985c2712.png)

Leetcode link: https://leetcode.com/problems/palindrome-partitioning-ii/


### Approach 2: Dynamic Programming, minCutOneDP()

Credit to: https://www.youtube.com/watch?v=lDYIvtBVmgo

This idea is to set up a 2d table `dp` where `dp[i][j]` stands for the min cuts needed to make `s[i:j]` a valid palindrome partitioning. Thus the final answer is located at `dp[0][n-1]` where `n` is the length of string `s`.



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
