# Climbing Stairs problem
* You are climbing a staircase. It takes `n` steps to reach the top.
* Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?


### Approach 1: Brute Force, climbStairsRecursion()
This is a brute force solution where we consider all possible paths that we can take to get to the top. At each step, we can either climb 1 step or 2 steps, if we've reach the top, increment the result counter and explore the next possible path.
This solution leads to TLE :(, not surprisingly


### Approach 2: Fibonacci, Recursion, climbStairsMath()
This solution is based on the calculation of fibonacci series. Because each value is equal to the sum of previous two values, we can use recursion with memorization to calculate the final result.\
![d2b2ae0820e71112812efd5c2220019](https://user-images.githubusercontent.com/25105806/130372380-a4d89d2c-9dd7-4a52-989c-b3fd97659c46.png)

### Approach 3: Fibonacci, Iteration1, climbStairsIteration1()
Instead of using recursion to calculate Fibonacci, we can also use iteration to calcualte. This approach stores all calculated values in the list.\
![c4cd90fa4eeb4d263b15558b8fd162a](https://user-images.githubusercontent.com/25105806/130372424-5832ee65-b7ee-4998-abdb-aa55b8b243c5.png)

### Approach 4: Fibonacci, Iteration2, climbStairsIteration2()
It is not hard to find out that the only two values matter are the immediate previous two values, all values in the past need not to be stored, so we can only use two variables `a` and `b` to store the previous two values and exchange value when calculating new value.\
![bba600022cd328a5b254c5bb614d8bd](https://user-images.githubusercontent.com/25105806/130372457-386eeb77-6335-44f0-b524-e10b989b1932.png)

