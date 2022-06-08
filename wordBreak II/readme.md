# Word Break II problem
![image](https://user-images.githubusercontent.com/25105806/172548648-d4d10a0a-115f-4987-b342-5b341bd565be.png)


Leetcode Link: https://leetcode.com/problems/word-break-ii/

<br />

### Approach 1: Backtracking, wordBreak(), backtrack(), backtrack2()
The idea is built upon [Word Break I](https://github.com/artisan1218/LeetCode-Solution/tree/main/wordBreak), where we will loop through the `wordDict`. This way, we only need to check the substrings with correct length and thus skipping lots of invalid substring. We will solve this recursively by entering another stack of recursion everytime we find one possible substring (length is within the length range of `s` and presented in the wordDict): `i + word.length() <= s.length() && s.substr(i, word.length()) == word`.

We can either use vector or string concatenation to do the backtrack. The purpose of backtracking is to revert once we found certain splits are not valid.

Implementation with vector:
```cpp
vector<string> wordBreak(string s, vector<string>& wordDict) {
    vector<string> cur, result;
    backtrack(s, wordDict, 0, cur, result);
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
```

<br />

Implementation with string concatenation:
```cpp
vector<string> wordBreak(string s, vector<string>& wordDict) {
    vector<string> result;
    backtrack2(s, wordDict, 0, "", result);
    return result;
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
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/172550030-b109baa1-a7e2-4f15-8993-907c4cb7a9dc.png)
