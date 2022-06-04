# Word Break problem
![image](https://user-images.githubusercontent.com/25105806/171986652-dab65881-781b-437a-93b9-55ed3868df65.png)

Leetcode link: https://leetcode.com/problems/word-break/

<br/>

### Approach 1: Dynamic Programming, wordBreakDP1()
We can find the sub-problem relationship between substring and string `s`. For example if `leet` can be found in `wordDict`, we only need to see if `code` exists without checking the entire `leetcode`. We use a vector `dp` to store the previous result. Since we only need to get the substring starting from the next index of previous valid position up to current index, we can use a `validIdxList` vector to store all indices of `true` result in `dp`, so that we don't need to loop over the entire `dp`.

<img src="https://user-images.githubusercontent.com/25105806/171986952-e772cf5a-4ffe-4f50-a3db-9942856b0c09.jpg" heigth="60%" width="60%">


Note that in this case, `DP[7]` is dicided by `s[0:8]` which is the entire substring up to `i` and `s[4:8]` which is the substring starting from the 'next index of preivous valid index', notice that `DP[3]==True`, the next substring we should check is `code`.

Full code:
```cpp
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
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/171987066-42626a23-4925-4dba-b255-6785cfc8bd86.png)


<br/>

### Approach 2: Dynamic Programming, wordBreakDP2()
Credits to: https://www.youtube.com/watch?v=Sx9NNgInc3A

This solution is similar to the first approach but we loop backward this way, and we will use a nested loop to loop through `wordDict` to see if current substring can be found in `wordDict`. By looping through `wordDict` we can know the length of substring we're looking for so there is no need to maintain another list to store the valid indices.

```cpp
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
```

Time complexity is O(m\*n) where m is the size of `wordDict` and n is the size of `s`:\
![image](https://user-images.githubusercontent.com/25105806/171987202-adb04e0e-161e-404e-a985-836ec9e24ce6.png)
