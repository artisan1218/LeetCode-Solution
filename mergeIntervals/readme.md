# Merge Intervals problem
* Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping `intervals` that cover all the intervals in the input.

Leetcode link: https://leetcode.com/problems/merge-intervals/

<br />

### Approach 1: Sort and Merge, merge()
We first sort all intervals in the `intervals` list so that they are in ascending order. Then start from the beginning compare the adjacent two intervals to see whether they should be merged, add the new merged intervals or left intervals to the result list and check the next pair.

```python3
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # sort the intervals so that the intervals are in order
    intervals.sort()
    # dummy intervals so that we dont need to handle the case where the last interval will not be added
    intervals.append([float('inf'), float('inf')])

    result = []
    leftInter = intervals[0]
    for rightInter in intervals[1:]:
        # if there is a pair of overlapping intervals, we will update the leftInter to be the merged intervals
        # and check the next right interval with the merged interval to see if there is still an overlapping
        if self.overlap(leftInter, rightInter):
            leftInter = [leftInter[0], max(leftInter[1], rightInter[1])]
        else:
            # there is no overlapping between left interval and right interval
            # we can safely append the left interval to the result list and check the next pair
            result.append(leftInter)
            leftInter = rightInter

    return result

def overlap(self, interval1, interval2):
    return not(interval1[1] < interval2[0])
```

Time complexity is O(nlogn):\
![e8c6610265705c842e39354f8f7cd61](https://user-images.githubusercontent.com/25105806/127718009-772dcf43-eb13-42bc-a412-141fa7745909.png)


