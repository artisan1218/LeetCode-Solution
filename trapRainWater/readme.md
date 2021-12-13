# Trapping Rain Water problem
* Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

![image](https://user-images.githubusercontent.com/25105806/145903558-6c9c8e78-cd0b-4011-9460-88a2dd3a6437.png)

Leetcode link: https://leetcode.com/problems/trapping-rain-water/

<br/>

### Approach 1: Calculate Level by Level, trapLevelByLevel(), Java
**Note: this solution is slow and lead to TLE**

The idea is simple. We scan horizontally from the highest bar in the elevation map `height`. If a bar is taller or equal to the level height, we denote it with 1, otherwise with 0, then for each level, we compute the amount of water trapped and sum them up for the final answer.

<img src="https://user-images.githubusercontent.com/25105806/123038940-21cc4880-d3a6-11eb-9e83-e75940ba8ca7.png" height="80%" width="80%">
<img src="https://user-images.githubusercontent.com/25105806/123038961-2abd1a00-d3a6-11eb-9812-c93d362d38aa.png" height="80%" width="80%">
<img src="https://user-images.githubusercontent.com/25105806/123038965-2c86dd80-d3a6-11eb-8577-66b4214d8ddb.png" height="80%" width="80%">


```java
// TLE
public int trapLevelByLevel(int[] height) {
    int result = 0;

    // get the tallest bar
    // O(n)
    int tallest = 0;
    for (int bar : height) {
  if (bar > tallest) {
      tallest = bar;
  }
    }

    // O(tallest) * O(n)
    while (tallest > 0) {
  // get each level and compute volume of water level by level
  int volume = 0;
  int temp = 0;
  boolean first = true;
  // O(n)
  for (int bar : height) {
      if (bar >= tallest) {
    // the bar is taller than current level, it is the boundary of a basin
    volume += temp;
    temp = 0;
    first = false;
      } else {
    // the bar is shorter than current level, it can trap water
    // as long as it is not the first bar
    if (!first) {
        temp += 1;
    }
      }
  }
  tallest -= 1;

  // add volume of water at this level
  result += volume;
    }

    return result;
}
```

Time complexit is `O(nlogn*tallest*n)` where `O(nlogn)` is used to find the tallest bar when sorting, `tallest` is the height of the tallest bar because we will scan from top to down, `n` is the length of the elevation map because we will calculate the amount of water trapped for each level.


<br />

### Approach 2: Divide and Conquer, trapCalculateFromTallestHeightRecursion(), calculateInterval(), Python
The idea is to first find the tallest two bars in the entire map, calculate the volume of water bounded by these two bars, then for the left and right interval of the two bars, we did the same calculation using recursion.\
For each recursion, we will first sort the interval bounded by `left` and `right`, this is to find the tallest two bars to calculate the volume of water. The sorting will take O(nlogn) time. In the best case where the left-most bar and right-most bar are tallest two bars, we only need to sort the entire map once and return the result.

1. First compute the volume bounded by the middle red block because 3 and 2 are two tallest bars in the entire elevation map
2. Then for the left interval of the middle red block, first compute the second-from-left red block, because 1 and 2 are the two tallest bars in the left interval
3. Then compute the first-from-left red block, which gives answer 0 because 0 and 1 do not trap any water
4. For the right interval, first compute second-from-right red block bounded by 2 and 2
5. Lastly, compute the last red block bounded by 2 and 1
6. Sum up the volume in each block will give the answer
<img src="https://user-images.githubusercontent.com/25105806/123039936-c4d19200-d3a7-11eb-8472-d485a13cb0a9.png" height="80%" width="80%">

```python
def trapCalculateFromTallestHeightRecursion(self, height: List[int]) -> int:
    left = 0
    right = len(height)-1
    return self.calculateInterval(height, left, right)

def calculateInterval(self, height: List[int], left: int, right: int) -> int:

    # only calculate the volume in this interval
    interval = height[left:right+1]

    # list of pair of (height of a bar, index of a bar)
    pairList = list()
    for idx, bar in enumerate(interval):
        pairList.append((bar, left + idx))
    # sorted list by height of the bar in descending order
    pairList = sorted(pairList, key=lambda pair:(-pair[0], pair[1]))
    # remove all bar with height 0 because they will not be able to trap any water
    pairList = [pair for pair in pairList if pair[0]>0]

    result = 0
    if len(pairList)>1:
        # take the tallest two bar and calculate the volume in this basin bounded by these two bars
        bar1Height = pairList[0][0]
        bar2Height = pairList[1][0]
        leftBarIdx = min(pairList[0][1], pairList[1][1])
        rightBarIdx = max(pairList[0][1], pairList[1][1])
        volume = min(bar1Height, bar2Height) * (rightBarIdx-leftBarIdx-1)
        # remove any blocks within this basin that cannot hold water
        for block in height[leftBarIdx+1:rightBarIdx]:
            volume -= block
        result += volume
    else:
        return 0

    # the tallest two bars are the outer-most two bar that covers all volume in this interval
    # there is no need to calculate anymore, just return the current volume
    if leftBarIdx==left and rightBarIdx==right:
        return result
    else:
        result += self.calculateInterval(height, left, leftBarIdx)
        result += self.calculateInterval(height, rightBarIdx, right)
        return result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/123039856-ac617780-d3a7-11eb-8f8a-51bf8b8f1f6b.png)


<br />

### Approach 3: Dynamic Programming, trapDP(), Python
Credits to: https://www.youtube.com/watch?v=ZI2z5pq0TqA

Turns out we only need to find the tallest bar from the left and tallest bar from right, take the minimum of the two at index `i` and minus the bar height at `i`.\
`leftMax` keeps track of the tallest bar in each i from left because the tallest bar will trap water along with the right tallest bar.
`rightMax` keeps track of the tallest bar in each i from right.

As the image below suggests, we can scan the map in two passes to obtain tallest bar from left and tallest bar from right. Then use another pass to calculate the result.
![trapping_rain_water](https://user-images.githubusercontent.com/25105806/123040673-fc8d0980-d3a8-11eb-8f06-fce845f8b162.png)

```python
def trapDP(self, height: List[int]) -> int:
    # scan from left to right, store the volume of water than can be stored with left boundary
    leftMax = list()
    currMax = 0
    for bar in height:
        currMax = max(bar, currMax)
        leftMax.append(currMax)

    # scan from right to left, store the volume of water than can be stored with right boundary 
    rightMax = list()
    currMax = 0
    for bar in reversed(height):
        currMax = max(bar, currMax)
        rightMax.append(currMax)
    rightMax.reverse()

    # the actual volume of water will be the minimum of two volumes minus the volume of blocks
    result = 0
    for i in range(len(height)):
        result += min(leftMax[i], rightMax[i]) - height[i]

    return result
```

Time complexity is therefore O(3\*n) which is O(n)\
![image](https://user-images.githubusercontent.com/25105806/123040807-352ce300-d3a9-11eb-8e24-813f6cee95b9.png)

