#!/usr/bin/env python
# coding: utf-8

# In[37]:


from typing import List

class Solution:
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
    
if __name__ == "__main__":
    solver = Solution()
    intervals = [[1,4],[2,3]]
    print(solver.merge(intervals))


# In[ ]:




