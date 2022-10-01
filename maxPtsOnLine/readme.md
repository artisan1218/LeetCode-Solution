# Max Points on a Line problem
![image](https://user-images.githubusercontent.com/25105806/193377312-b29adde9-0223-4e1b-a2a8-5cfbb772c946.png)


Leetcode Link: https://leetcode.com/problems/max-points-on-a-line/

<br />

### Approach 1: Math, Calculate Slope, maxPoints()

The idea based on slope, which is the ratio of delta y and delta x between two points. We can calculate the slope between all pairs of points in `points`, and therefore we will know the number of points with the same slope. However, this is not enough to decide whether they are on a same line. When calculating the slope of two points, we also need to keep track of the `src` point of a line, so if some points share a same slope and a src point, they must on the a same line. 

We use nested loop to do this. The first loop is to loop through all points and make them as source point and the second loop to loop through all remaining points to calculate the slope between them and source point. We will keep the max number of points for each source point and simply return the max value. 

```python3
def maxPoints(self, points: List[List[int]]) -> int:
    if len(points)<=2:
        return len(points)
    else:
        # calculate slopes between all pairs in the points, if two pairs have the same slope and start with a same point, they are on the same line
        curMax = 0
        for src in points:
            # slopeDict:
            # key: slope between src and dst
            # value: number of dst points that fall on the line that starts with src
            # so slopeDict contains the number of points on a line starts with different src point
            slopeDict = dict()
            for dst in points:
                if src!=dst:
                    # calculate slope
                    delta_x = dst[0] - src[0]
                    delta_y = dst[1] - src[1]
                    slope = float('inf') if delta_x == 0 else delta_y / delta_x

                    if slope in slopeDict:
                        slopeDict[slope]+=1
                    else:
                        slopeDict[slope]=2
            curMax = max(curMax, max(slopeDict.values()))

        return curMax
```

Time complexity is O(n^2):

![image](https://user-images.githubusercontent.com/25105806/193377515-9232038a-6705-4c9f-a173-95d6fc82593a.png)
