#!/usr/bin/env python
# coding: utf-8

# In[12]:


from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # calculate the time needed for each car to reach target point
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
   
        # the key point is that the speed of head car in each fleet WON'T change
        # so when going from back to beginning, we only need to consider the greater time than current time
        fleets = 0
        curTime = 0
        for t in time[::-1]:
            if t > curTime:
                fleets += 1
                curTime = t
        return fleets
        
        
if __name__ == '__main__':
    solver = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    result = solver.carFleet(target, position, speed)
    print(result)


# In[ ]:




