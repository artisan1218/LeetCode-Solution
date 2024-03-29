# Container With Most Water problem
* Given n non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Leetcode link: https://leetcode.com/problems/container-with-most-water/

<br/>

### Approach 1: Brute Force, Skipped
The most simple yet inefficient approach is to calculate every possible combinations of two lines and keep the value of max area. This approach is skipped.

### Approach 2: Two Pointers, maxArea()
Turns out we can use two pointers `left` and `right` to bound the sides and form a container. `left` starts at index `0` and `right` starts at index `height.length - 1`.\
We will move `left` and `right` inward keep the max area.


   ![maxAreaAnimation](https://user-images.githubusercontent.com/25105806/121755812-00797b80-cacd-11eb-80e4-129c40acb153.gif)

**Note:Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/solutions/maxArea/maxAreaAnimation.ppsx) to download the animation to play for yourself**


```java
public static int maxArea(int[] height) {
	int left = 0, right = height.length - 1, max = 0, bottom = height.length - 1;
	while (left < right) {
	    int side = Math.min(height[left], height[right]);
	    max = Math.max(max, side * bottom);
	    if (height[left] < height[right]) {
		left++;
	    } else {
		right--;
	    }
	    bottom = bottom - 1;
	}
	return max;
    }
```


<br />

Time complexity is O(n) because the two pointers altogether will iterate through each side of the `height` and the program will end as soon as they meet. Space complexity is O(1) because all we need to store is the left and right side of the container.

![image](https://user-images.githubusercontent.com/25105806/118609194-5c234400-b76f-11eb-9657-8a2d0b0900c8.png)


