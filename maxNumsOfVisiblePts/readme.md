# Maximum Number of Visible Points problem
![image](https://user-images.githubusercontent.com/25105806/136468456-19059f8d-4930-438c-ac48-671e1927c896.png)
![image](https://user-images.githubusercontent.com/25105806/136468484-cce6dbed-d22e-4cb0-b2d4-b58909759d79.png)

Leetcode link: https://leetcode.com/problems/maximum-number-of-visible-points/

<br />

### Approach 1: Convert to Polar Coordinates, visiblePoints()
The solution involves a little bit of geometry, we need to first convert the points in `[x, y]` coordinates to polar coordinates so that we can easily compare it with the field of view `angle`.

Then simply use a sliding window to count the max number of points in side the range of `angle`.

```python
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
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/136468833-0955fe73-9216-49a8-8395-d1fd2419e227.png)
