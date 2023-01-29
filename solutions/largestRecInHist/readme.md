# Largest Rectangle in Histogram problem
* Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

<img width="611" alt="image" src="https://user-images.githubusercontent.com/25105806/133164438-29b0084b-d72a-4097-8791-667f9196993b.png">

Leetcode link: https://leetcode.com/problems/largest-rectangle-in-histogram/

<br/>

### Approach 1: Monotonic Stack, largestRectangleArea1()
Credits to: https://www.youtube.com/watch?v=zx5Sw9130L0

This solution utilized monotonic stack where we only append new pair of elements (index, height) when the height of current bar is higher than the height of last bar in stack, that's why it is monotonic increasing. When we have a bar that is lower than the height of bar on top of stack we pop the lower bar out of the stack and calculate the area of max rectangle. Then we check the remaining the bar in the stack after all bars have been visited. Since the remaining bar are guranteed to be in increasing order, the width is simply the total length of the heights.

```python
def largestRectangleArea1(self, heights: List[int]) -> int:
    if len(heights)==0:
        return 0
    else:
        maxArea = 0
        stack = [] # monotonic stack

        for i, h in enumerate(heights):
            start = i
            # when we have a bar that is lower than the height of bar on top of stack
            # we pop the lower bar out of the stack and calculate the area of max rectangle
            while len(stack)!=0 and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            # we only push the index, height pair when the current bar is higher than
            # the height of bar on top of stack, this is why it's monotonic
            stack.append((start, h)) 

        # check the remaining the bar in the stack
        # since the remaining bar are guranteed to be in increasing order, the width is simply
        # the total length of the heights
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights)-idx))

        return maxArea
```

Time complexity is O(n):\
<img width="666" alt="image" src="https://user-images.githubusercontent.com/25105806/133164866-716f757e-e134-49cd-9a5a-cc0b6f2febde.png">

<br/>

### Approach 2: Monotonic Stack, largestRectangleArea2()
Same idea as approach 1, but uses different ways of implementation. Instead of storing both index and height, we store only the index. The key part is the code below:
```
width = i if len(stack)==0 else (i-stack[-1]-1)
```
This controls the width of the current bars, which means, to which bar do we extend the width. If there is still a bar in the stack after popping the current one, then that means we can only extend the width up to the previous bar, otherwise extend all the way to 0, which is simply `i`

```python
def largestRectangleArea2(self, heights: List[int]) -> int:
    if len(heights)==0:
        return 0
    else:
        maxArea = 0
        stack = [] # monotonic stack
        # instead of storing both index and height, we only store index
        for i in range(len(heights)):
            while len(stack)!=0 and heights[stack[-1]]>heights[i]:
                idx = stack.pop()
                width = i if len(stack)==0 else (i-stack[-1]-1)
                maxArea = max(maxArea, heights[idx] * width)
            stack.append(i)

        while len(stack)!=0:
            idx = stack.pop()
            width = len(heights) if len(stack)==0 else (len(heights)-stack[-1]-1)
            maxArea = max(maxArea, heights[idx] * width)

        return maxArea
```

Time complexity is still O(n):\
![image](https://user-images.githubusercontent.com/25105806/133554483-a86e73d1-3dda-4192-9746-524b0b9e732b.png)
