# Visiting Cities problem

There are two bus routes `red` and `blue`, represented in an array. 

Each index represents a city and each index value represents the cost to reach that index from previous city. You start from city at index 0. There is an additional blue cost applied when you change route from red to blue or start from blue. Staying on the blue route doesnt incur any blue cost.

Return the minimum cost of reaching each city i.e each index. from city 0.

Example:\
Input:\
red = [2, 1, 4, 5]\
blue = [3, 2, 1, 2]\
blueCost = 2


Output: [0, 2, 3, 6, 8]\
Explanation: Because we are starting from index 0 to reach it we need 0 cost.\
Then we take red route because its minimum so 2, then again red so 2+1 = 3, then we change route to blue route with blue cost so 3+1+2 = 6, then continue on blue to reach end 6+2 = 8

<br />

### Approach 1: Dynamic Programming, minCost()

Although it may be easy to think of a greedy solution when looking at the description, the greedy solution actually does not work because we cannot know whether there are stops in the future with less costs end up in a less total cost, even though it is not the least cost stop for now. 

Therefore we should consider using dynamic programming algorithm that takes both red and blue lines into consideration when computing and comparing the costs.

`dp_r` and `dp_b` are costs for red line and blue line, respectively. We will loop through both lines, then for red line, we will calculate these and take the minimum:
1.  the cost of going from previous red stop to current red stop
2.  the cost of going from previous blue stop to current red stop

for blue line, similarly, we will calculate these and take the minimum:
1.  the cost of going from previous blue stop to current blue stop
2.  the cost of going from previous red stop to current red stop

then simply store the minimum cost at current stop from the two dp arrays. 

The reason we use two lists to store blue and red cost separately is that we cannot make sure the local optimal choice will lead to global optimal path. So we have to store all (blue and red lines cost at each stop) costs.

```python3
def minCost(red, blue, blueCost):
    ans = [0]
    
    dp_r = [0 for i in range(len(red)+1)]
    dp_b = [0 for i in range(len(blue)+1)]
    dp_b[0] = blueCost
    for i in range(1, len(red)+1):
        dp_r[i] = min(dp_r[i-1] + red[i-1], dp_b[i-1] + red[i-1]) # r2r, b2r
        dp_b[i] = min(dp_b[i-1] + blue[i-1], dp_r[i-1] + blue[i-1] + blueCost) # b2b, r2b
        ans.append(min(dp_r[i], dp_b[i]))
            
    return ans
```

The time complexity is O(n) as we only go through each list once.
