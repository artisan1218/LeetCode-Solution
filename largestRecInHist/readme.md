# Largest Rectangle in Histogram problem
* Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

<img width="611" alt="image" src="https://user-images.githubusercontent.com/25105806/133164438-29b0084b-d72a-4097-8791-667f9196993b.png">



### Approach 1: Monotonic Stack, largestRectangleArea()
Credits to: https://www.youtube.com/watch?v=zx5Sw9130L0

This solution utilized monotonic stack where we only append new pair of elements (index, height) when the height of current bar is higher than the height of last bar in stack, that's why it is monotonic increasing. When we have a bar that is lower than the height of bar on top of stack we pop the lower bar out of the stack and calculate the area of max rectangle. Then we check the remaining the bar in the stack after all bars have been visited. Since the remaining bar are guranteed to be in increasing order, the width is simply the total length of the heights.

Time complexity is O(n):

<img width="666" alt="image" src="https://user-images.githubusercontent.com/25105806/133164866-716f757e-e134-49cd-9a5a-cc0b6f2febde.png">

