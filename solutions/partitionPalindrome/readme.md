# Palindrome Partitioning problem
<img width="547" alt="image" src="https://user-images.githubusercontent.com/25105806/161417246-137a44ae-1776-4bd3-bc3a-4325934eb374.png">

Leetcode link: https://leetcode.com/problems/palindrome-partitioning/

<br />

### Approach 1: Backtracking, partition(), dfs(), isPalindrome()

Reference: https://www.youtube.com/watch?v=3jvWodd7ht0 and https://leetcode.com/problems/palindrome-partitioning/solution/

The idea is to first generate all possible ways of partitioning the string `s`. This can be done by using dfs. Then after each possible partitioning, check if the substring is a valid palindrome by calling isPalindrome(). If the substring is valid, then we first add it to a temp vector, then calling dfs on the remaining substring of `s`, then we backtrack the current substring by removing it from the temp vector, so that it will not affect the next possible way of partition.
<img width="887" alt="image" src="https://user-images.githubusercontent.com/25105806/161417358-66492000-a878-44ff-9fc6-7e485d38832f.png">

```cpp
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
```

Time complexity is O(n\*2^n) because there are 2^n ways to partition the string and each of them takes O(n) to check for palindrome:\
<img width="673" alt="image" src="https://user-images.githubusercontent.com/25105806/161418210-4c642152-3752-49f1-8503-cebe196db444.png">
