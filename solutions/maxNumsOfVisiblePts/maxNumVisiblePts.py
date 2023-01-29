#!/usr/bin/env python
# coding: utf-8

# In[11]:


from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        pointsAngle = list()
        same = 0
        for point in points:
            if point[0]==location[0] and point[1]==location[1]:
                same+=1
            else:
                # convert each point to its polar coordinates
                convertedAngle = math.atan2(point[1]-location[1], point[0]-location[0])
                pointsAngle.append(convertedAngle)
        
        # scale points in the converted coordinates and viewing angle
        pointsAngle.sort()
        pointsAngle = pointsAngle + [point + 2.0 * math.pi for point in pointsAngle]
        angle = math.pi * angle / 180
        
        # use a sliding window to calculate the max number of visible points
        result = same # we always see the points that are on the same spot as ourselves
        left = 0
        for right in range(len(pointsAngle)):
            while pointsAngle[right] - pointsAngle[left] > angle:
                # we cannot see all points with the range [left, right], so we have to move left pointer to right
                left += 1
            result = max(result, same+right-left+1)
            
        return result

if __name__ == '__main__':
    solver = Solution()
    points = [[2,1],[2,2],[3,3]]
    angle = 90
    location = [1,1]
    number = solver.visiblePoints(points, angle, location)
    print(number)

