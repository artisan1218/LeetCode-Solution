# Container With Most Water problem
* Given n non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

### Approach 1: Brute Force, Skipped
The most simple yet inefficient approach is to calculate every possible combinations of two lines and keep the value of max area. This approach is skipped.

### Approach 2: Two Pointers, maxArea()
Turns out we can use two pointers `left` and `right` to bound the sides and form a container. `left` starts at index `0` and `right` starts at index `height.length - 1`.\
We will move `left` and `right` inward keep the max area.
Time complexity is O(n) because the two pointers altogether will iterate through each side of the `height` and the program will end as soon as they meet. Space complexity is O(1) because all we need to store is the left and right side of the container.

![image](https://user-images.githubusercontent.com/25105806/118609194-5c234400-b76f-11eb-9657-8a2d0b0900c8.png)


