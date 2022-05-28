# Palindrome Partitioning III problem
![image](https://user-images.githubusercontent.com/25105806/170843965-a19ba15f-6d0c-4866-a2dc-90e967358a9d.png)

Leetcode link: [https://leetcode.com/problems/partition-list/](https://leetcode.com/problems/palindrome-partitioning-iii/)

<br />

### Approach 1: Brute Force, palindromePartitionNaive()
This is the brute force solution and the idea is to first get all possible ways of splitting string `s` into `k` substrings. We do this by using DFS exhaustively. Then for each valid split, we calculate the minimum changes needed to convert them to palindromes and keep the minimum change as the result.

```cpp
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
```

Time complexity is O(n^3) because we need O(n^2) to get all splits and O(n) to calculate the minimum number of changes. Therefore it leads to TLE.

<br />

### Approach 2: Memorization DP, palindromePartitionDFSmem()
Credits to: https://leetcode.com/problems/palindrome-partitioning-iii/discuss/441427/Python3-Top-down-DFS-with-Memoization

The idea is to use memorization to skip duplicate calculations. Consider the case where `s="aabcde", k=4`:


<img src="https://user-images.githubusercontent.com/25105806/170844728-4002385c-a1e1-4875-820e-c4cf4ab536ad.jpg" width="60%" height="60%">

Here are all possible 4 splits of the string `s`. Notice that when we first enter the loop and start splitting, in the first iteration(right=1, which means first split is `a`), we calculated the min costs of splitting `cde` into 2 parts(marked in red). However, in the second iteration(right=2, first split is `aa`), we calculated the min cost for `cde` and `k=2` again. This means there will be more duplicates in the even longer string and larger k. Therefore we can cache the result of the first calculation and use it right away in the second duplicate case. 

The duplicate `cde` and `k=2` means we need to split substring `cde` into `k=2` parts and calculate the min cost of converting all parts to palindrome. Therefore we can use a map to store the result and use the index('left` in the code) of the substring and k as the key. We need to find a way to combine both index and k because in c++, we cannot use tuple as the map key, so we can simply concatenate the two int as a string `to_string(left) + "-" + to_string(k)`. 

Full code:

```cpp
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
```

Time complexity is O(n^2k):\
![image](https://user-images.githubusercontent.com/25105806/170844755-62d92991-b85a-4b58-af39-12b3e5393e19.png)
