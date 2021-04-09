# Longest Substring Without Repeating Characters problem
* Given a string s, find the length of the longest substring without repeating characters.


### Approach 1: brute force, skipped

### Approach 2: sliding window, lengthOfLongestSubstring()
Use two pointer(left and right) to bound a sliding window in which each character is unique. Use a map to keep track of the seen char and corresponding index, map has a constant look up time so it only takes O(1) to check if the new char already existed in current sliding window. If the new char is not in map, simply add it to the map and increment the current length, if not, update the left pointer position according to the new char's index and existing char's index in the map, so that we can avoid removing char from the map, which saves O(n) time.

