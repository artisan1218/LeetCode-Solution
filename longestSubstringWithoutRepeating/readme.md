# Longest Substring Without Repeating Characters problem
* Given a string `s`, find the length of the longest substring without repeating characters.

Leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

<br />

### Approach 1: brute force, skipped
Use nested loop to go through each possible substring, count their length and keep the longest one. It takes another O(n) to check if a char exists in current substring, so total time complexity is O(n^3), space complexity is O(1)

<br />

### Approach 2: sliding window, lengthOfLongestSubstring()
Use two pointer(left and right) to bound a sliding window in which each character is unique. Use a map to keep track of the seen char and corresponding index, map has a constant look up time so it only takes O(1) to check if the new char already existed in current sliding window. If the new char is not in map, simply add it to the map and increment the current length, if not, update the left pointer position according to the new char's index and existing char's index in the map, so that we can avoid removing char from the map, which saves O(n) time. 

![lengthOfLongestSubstringAnimation](https://user-images.githubusercontent.com/25105806/121754374-54826100-cac9-11eb-9dc5-2a9ca808b3c6.gif)


**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/longestSubstringWithoutRepeating/lengthOfLongestSubstringAnimation.ppsx) to download the animation to play for yourself**


```java
public static int lengthOfLongestSubstring(String s) {
    int longestLen = 0;
    int currLen = 0;
    int left = 0; // left pointer
    int right = 0; // right pointer
    // map that keeps track of each char and the corresponding index
    Map < Character, Integer > charIdxMap = new HashMap < > ();
    for (right = 0; right < s.length(); right++) {
        // get the current char
        char currChar = s.charAt(right);
        if (!charIdxMap.containsKey(currChar)) { // new char
            // if this is a new char, simply increment the current length
            currLen++;
        } else {
            // not a new char, then update the position of left pointer
            // so that the left and right form a proper window in which each char is unique
            // do not need to remove char that are not in the current window from the map
            // simply compare the index with left, if index is smaller, then the window does
            // not include that char, otherwise update left to the char's index
            left = Math.max(charIdxMap.get(currChar) + 1, left);
            currLen = right - left + 1;
        }
        // update the map with new char's index or add a new char-index pair
        charIdxMap.put(currChar, right);
        longestLen = Math.max(currLen, longestLen);
    }
    return longestLen;
}
```

<br />

Since we only go through the string once and store every char to the map, time complexity is O(n) and space complexity is also O(n)

![image](https://user-images.githubusercontent.com/25105806/118186766-f4799b80-b3f2-11eb-81ba-40b1c5ca5d60.png)
