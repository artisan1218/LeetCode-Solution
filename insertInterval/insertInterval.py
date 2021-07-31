#!/usr/bin/env python
# coding: utf-8

# In[126]:


from typing import List

class Solution:
    
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
    
if __name__ == "__main__":
    solver = Solution()
    intervals = []
    newInterval = [5,7]
    result = solver.insertFindLeftRight(intervals, newInterval)
    print(result)


# In[116]:


intervals = [[0,2]]
newInterval = [4,8]

s, e = newInterval[0], newInterval[1]
left = [i for i in intervals if i[1] < s]
right = [i for i in intervals if i[0] > e]


left


# In[117]:


right


# In[ ]:




