# Trapping Rain Water problem
* Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

  ![image](https://user-images.githubusercontent.com/25105806/123037788-20018580-d3a4-11eb-91c8-ed3add250a40.png)


### Approach 1: Calculate Level by Level, trapLevelByLevel(), Java
**Note: this solution is slow and lead to TLE**
The idea is simple. We scan horizontally from the highest bar in the elevation map `height`. If a bar is taller or equal to the level height, we denote it with 1, otherwise with 0, then for each level, we compute the amount of water trapped and sum them up for the final answer.

<img src="https://user-images.githubusercontent.com/25105806/123038940-21cc4880-d3a6-11eb-9e83-e75940ba8ca7.png" height="80%" width="80%">
<img src="https://user-images.githubusercontent.com/25105806/123038961-2abd1a00-d3a6-11eb-9812-c93d362d38aa.png" height="80%" width="80%">
<img src="https://user-images.githubusercontent.com/25105806/123038965-2c86dd80-d3a6-11eb-8577-66b4214d8ddb.png" height="80%" width="80%">


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

Time complexity is therefore O(3\*n) which is O(n)\
![image](https://user-images.githubusercontent.com/25105806/123040807-352ce300-d3a9-11eb-8e24-813f6cee95b9.png)

