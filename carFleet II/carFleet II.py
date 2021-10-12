#!/usr/bin/env python
# coding: utf-8

# In[18]:


from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = list()
        n = len(cars)
        result = [-1] * n
        
        # scan from right to left
        for i in range(n-1, -1, -1):
            pos, speed = cars[i]
            # monotonic stack
            while len(stack)!=0:
                headCarSpeed = stack[-1][2]
                if speed<=headCarSpeed:
                    stack.pop()
                else:
                    collisionTime = (stack[-1][1] - pos) / (speed - headCarSpeed)
                    if collisionTime >= result[stack[-1][0]] > 0:
                        stack.pop()
                    else:
                        break
                
            if len(stack)!=0:
                result[i] = (stack[-1][1] - pos) / (speed - stack[-1][2])
        
            stack.append((i, pos, speed))
        
        return result
    
    
if __name__ == '__main__':
    solver = Solution()
    cars = [[3,4],[5,4],[6,3],[9,1]]
    result = solver.getCollisionTimes(cars)
    print(result)


# In[ ]:




