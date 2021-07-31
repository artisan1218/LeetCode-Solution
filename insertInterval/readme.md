# Insert Interval problem
* Given a set of `non-overlapping` intervals, insert a new interval into the intervals (merge if necessary).
* You may assume that the intervals were initially sorted according to their start times.

### Approach 1: Insert newInterval and Merge, insertInsertAndMerge()
We first find the insertion place of the `newInterval` by scanning the `intervals` from left, insert `newInterval` into the `intervals`, then simply use the same logic as the [mergeInterval](https://github.com/artisan1218/LeetCode-Solution/tree/main/mergeIntervals): merging adjacent two intervals until two intervals are not overlapping anymore

Time complexity is O(n):

![53b710a4fe3b2b1a9dc7ab85a90a65d](https://user-images.githubusercontent.com/25105806/127731876-a351a74e-4193-4e4f-9d1d-557c0bce3d29.png)


### Approach 2: Find Left and Right Intervals then Combine, insertFindLeftRight()
Credits to: https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions


The idea is to first find the left and right part of the intervals of the `newInterval`, then combine the middle intervals as merged interval and connect all three parts together to form the result. 

To find the left intervals, we need to find all intervals with ending digit smaller than the beginning digit of `newInterval`:\
`left = [inter for inter in intervals if inter[1] < newInterval[0]]`

To find the rigth intervals, we need to find all intervals with beginning digit bigger than the ending digit of `newInterval`:\
`right = [inter for inter in intervals if inter[0] > newInterval[1]]`

Time complexity is O(n):

![image](https://user-images.githubusercontent.com/25105806/127732033-6da33061-ca4e-4f07-96d7-098b8f33f285.png)
