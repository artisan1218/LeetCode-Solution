# Car Fleet problem
![image](https://user-images.githubusercontent.com/25105806/137034682-85f2741c-0c93-448a-b131-7568083b6e8c.png)

Leetcode link: https://leetcode.com/problems/car-fleet/

<br />

### Approach 1: Scan from Right to Left, carFleet()
Credits to: https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward and https://www.youtube.com/watch?v=H5w6doOXz10

The idea is to first calculate the time needed for each car to reach `target` point, then going from right to left of the time list, check for the new max time and count the number.
The key point is that the speed of head car of each fleet does not change, so we only need to consider the speed of head car. Since each fleet will not collide, the fleet to the left will be slower or equal to the fleet on the right. So we go from right to left, check the number of greater time needed to reach the `target`.

```python
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
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/137035218-59548320-8f71-472f-979b-eb9ff8c60fe6.png)
