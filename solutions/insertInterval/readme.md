# Insert Interval problem
* Given a set of `non-overlapping` intervals, insert a new interval into the intervals (merge if necessary).
* You may assume that the intervals were initially sorted according to their start times.

Leetcode link: https://leetcode.com/problems/insert-interval/

<br />

### Approach 1: Insert newInterval and Merge, insertInsertAndMerge()
We first find the insertion place of the `newInterval` by scanning the `intervals` from left, insert `newInterval` into the `intervals`, then simply use the same logic as the [mergeInterval](https://github.com/artisan1218/LeetCode-Solution/tree/main/mergeIntervals): merging adjacent two intervals until two intervals are not overlapping anymore.

```python3
def insertInsertAndMerge(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals)==0:
        return [newInterval]

    # since the intervals list is sorted, we can start search directly :)
    # search by the starting index of the interval
    insertIndex = 0
    for curInterval in intervals:
        # find the first occurence interval that fit newInterval
        if newInterval[0] > curInterval[0]:
            insertIndex+=1
        elif newInterval[0] == curInterval[0] and newInterval[1] > curInterval[1]:
            # sort based on the second digit of the interval if the frist digit is the same
            insertIndex+=1
        else:
            break

    # add new interval to the intervals list so that we can start merging
    intervals.insert(insertIndex, newInterval)  

    if insertIndex!=0:
        # if insertion place is not 0, we should set leftInter to the left interval because we need
        # to check the left interval with new interval first
        leftInter = intervals[insertIndex-1]
        rightInter = newInterval
    else:
        # if the insertion index is 0, leftInter is simply newInterval
        # rightInter is the second interval in the intervals list
        # note that the first interval is the newly inserted newInterval
        leftInter = newInterval
        rightInter = intervals[1]
        # increment insertIndex by 1 so that in merge() function, rightInter can start at correct index
        insertIndex+=1


    # depend on the insertion place, leftInter and rightInter can be different 
    if self.overlap(leftInter, rightInter):
        # start merging left and right intervals
        mergedInterval, delete_num = self.merge(intervals, insertIndex, leftInter)
        # decrement insertion place by 1 because there is overlapping in current left and right
        # we need to pop the newInterval out of the intervals list
        insertIndex-=1
    else:
        # new interval do not overlap with left interval
        # now we should check the newInterval with rightInter
        # so leftInter is now newInter and rightInter will be assigned in merge function
        # Note that insertIndex starts at insertIndex+1, this is to ensure rightInter is
        # one interval to the right
        leftInter = newInterval
        mergedInterval, delete_num = self.merge(intervals, insertIndex+1, leftInter)

    # to remove the merged intevals
    if delete_num > 0:
        for i in range(delete_num+1):
            intervals.pop(insertIndex)
        intervals.insert(insertIndex, mergedInterval)
    return intervals

def overlap(self, interval1, interval2):
    return not(interval1[1] < interval2[0])

def merge(self, intervals, insertIndex, leftInter):
    delete_num = 0
    for rightInter in intervals[insertIndex:]:
        # if there is a pair of overlapping intervals, we will update the leftInter to be the merged intervals
        # and check the next right interval with the merged interval to see if there is still an overlapping
        if self.overlap(leftInter, rightInter):
            delete_num+=1
            leftInter = [leftInter[0], max(leftInter[1], rightInter[1])]
        else:
            # there is no overlapping between left interval and right interval
            # no need to check the rest since they are non-overlapping
            break
    return leftInter, delete_num
```


Time complexity is O(n):\
![53b710a4fe3b2b1a9dc7ab85a90a65d](https://user-images.githubusercontent.com/25105806/127731876-a351a74e-4193-4e4f-9d1d-557c0bce3d29.png)

<br />

### Approach 2: Find Left and Right Intervals then Combine, insertFindLeftRight()
Credits to: https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions


The idea is to first find the left and right part of the intervals of the `newInterval`, then combine the middle intervals as merged interval and connect all three parts together to form the result. 

To find the left intervals, we need to find all intervals with ending digit smaller than the beginning digit of `newInterval`:\
`left = [inter for inter in intervals if inter[1] < newInterval[0]]`

To find the rigth intervals, we need to find all intervals with beginning digit bigger than the ending digit of `newInterval`:\
`right = [inter for inter in intervals if inter[0] > newInterval[1]]`

```python3
def insertFindLeftRight(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
    # find the left and right intervals of the new intervals
    left = [inter for inter in intervals if inter[1] < newInterval[0]]
    right = [inter for inter in intervals if inter[0] > newInterval[1]]

    if len(left) + len(right) == len(intervals):
        # there is no need to merge any intervals, simply insert the new interval
        return left + [newInterval] + right
    else:
        start = min(intervals[len(left)][0], newInterval[0])
        end = max(intervals[len(intervals)-len(right)-1][1], newInterval[1])
        return left + [[start, end]] + right
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/127732033-6da33061-ca4e-4f07-96d7-098b8f33f285.png)
