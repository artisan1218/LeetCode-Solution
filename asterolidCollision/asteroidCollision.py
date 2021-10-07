#!/usr/bin/env python
# coding: utf-8

# In[36]:


from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for asteroid in asteroids:
            if len(stack)==0:
                stack.append(asteroid)
            else:
                # same dir
                if (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0):
                    stack.append(asteroid)
                else:
                    # different dir
                    if stack[-1]<0 and asteroid>0:
                        # will not meet
                        stack.append(asteroid)
                    else:
                        asteroidExploded = False
                        while len(stack)>0 and asteroidExploded==False and stack[-1]>0 and asteroid<0:
                            if stack[-1] == abs(asteroid):
                                stack.pop()
                                asteroidExploded = True
                            elif stack[-1] < abs(asteroid):
                                stack.pop()
                            else:
                                asteroidExploded = True
        
                        if not asteroidExploded:
                            stack.append(asteroid)
        return stack
        
if __name__ == '__main__':
    solver = Solution()
    asteroids = [1,-2,-2,-2]
    result = solver.asteroidCollision(asteroids)
    print(result)


# In[ ]:




