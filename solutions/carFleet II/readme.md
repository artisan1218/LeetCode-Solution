# Car Fleet II problem
![image](https://user-images.githubusercontent.com/25105806/137035455-141e409f-e578-4870-8bc4-f4af5f35bf2d.png)

Leetcode link: https://leetcode.com/problems/car-fleet-ii/

<br />

### Approach 1: Scan from Right to Left, getCollisionTimes()
Credits to: https://www.youtube.com/watch?v=fH_hCzKNaGM and https://leetcode.com/problems/car-fleet-ii/discuss/1085987/JavaC%2B%2BPython-O(n)-Stack-Solution

Similar to [carFleet](https://github.com/artisan1218/LeetCode-Solution/tree/main/carFleet), we still going from right to left. Then we calculate the collsion time for each car with the car ahead of it. If the speed of current car is slower or equal to the car ahead of it, we should 'pop' the head car and check for the next car until we found a car that's slower than current car. If the collision time of current car with the head car is greater than the collsion time of head car, we should also 'pop' the head car because the collision with head car will happen after the head car collide with its head car. Since the head car's speed won't change, we can use the new head car's speed to calculate the collision time. 

```python
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
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/137036001-87c6a857-69e4-4bb6-89cc-ead05c44c90a.png)
