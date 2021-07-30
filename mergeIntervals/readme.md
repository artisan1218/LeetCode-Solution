# Merge Intervals problem
* Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping `intervals` that cover all the intervals in the input.


### Approach 1: Sort and Merge, merge()
We first sort all intervals in the `intervals` list so that they are in ascending order. Then start from the beginning compare the adjacent two intervals to see whether they should be merged, add the new merged intervals or left intervals to the result list and check the next pair.

![e8c6610265705c842e39354f8f7cd61](https://user-images.githubusercontent.com/25105806/127718009-772dcf43-eb13-42bc-a412-141fa7745909.png)


