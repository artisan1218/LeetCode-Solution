# Longest Common Prefix problem
* Write a function to find the longest common prefix string amongst an array of strings.
* If there is no common prefix, return an empty string `""`.

Leetcode link: https://leetcode.com/problems/longest-common-prefix/

<br/>


### Approach 1: Horizontal Scanning, longestCommonPrefix(), Java
Since the common prefix is a substring that each string in `strs` will have, we can simply iterate through the `strs`, decide the common prefix pair by pair and keep the shortest one.

```java
public static String longestCommonPrefix(String[] strs) {
	// since 1 <= strs.length <= 200, we can always set the first str to be the
	// longest common prefix at the very beginning
	String result = strs[0];

	for (int i = 1; i < strs.length; i++) {
	    String compStr = strs[i];
	    StringBuilder curr = new StringBuilder("");
	    String shorter = result.length() < compStr.length() ? result : compStr;

	    // compare each string with current result, decide their common prefix
	    for (int j = 0; j < shorter.length(); j++) {
		if (result.charAt(j) == compStr.charAt(j)) {
		    curr.append(shorter.charAt(j));
		} else {
		    break;
		}
	    }

	    // keep only the shortest common prefix
	    if (curr.length() < result.length()) {
		result = curr.toString();
	    }
	    if (result.length() == 0) {
		return "";
	    }
	}

	return result;
    }
```

![image](https://user-images.githubusercontent.com/25105806/118737282-5ffba880-b7f9-11eb-8f8d-ff5813dd8383.png)

<br/>

### Approach 2: Vertical Scanning, longestCommonPrefixVertical(), Python
We can easily and quickly decide the shortest string using `min()` function in python and check all chars at each string before the index of len of shortest string. E.g. if `"ab"` is the shortest string, then the common prefix must not exceed the length of 2, we can then check index 0 and index 1 for all strings to see if they are all equal.

```python
def longestCommonPrefixVertical(strs) -> str:
    result = ''
    minLen = min(strs, key=len)
    for i in range(len(minLen)):
        c = [word[i] for word in strs]
        if len(set(c)) == 1:
            result = strs[0][:i+1]
        else:
            break
    
    return result
```

![image](https://user-images.githubusercontent.com/25105806/118737572-f0d28400-b7f9-11eb-8f2a-42209dbfb7cc.png)

<br/>

### Approach 3: Vertical Scanning using zip(), longestCommonPrefixZip(), longestCommonPrefixZip2(), Python
The built in function `zip()` in Python can be used to perform the vertical scanning operation as we want. The idea is to get the 'column' of all strings char by char and to see if the column contains all equal chars. 

```python
def longestCommonPrefixZip(strs) -> str:
    result = ''
    for idx, columnTuple in enumerate(zip(*strs)):
        if len(set(columnTuple)) == 1:
            result = strs[0][:idx+1]
        else:
            break
    
    return result

def longestCommonPrefixZip2(strs) -> str:
    result = ''
    for idx, columnTuple in enumerate(zip(*strs)):
        if len(set(columnTuple)) > 1:
            return strs[0][:idx]

    return min(strs, key=len)
```

![image](https://user-images.githubusercontent.com/25105806/118738886-f1b8e500-b7fc-11eb-92fd-2b59cd9afebf.png)
