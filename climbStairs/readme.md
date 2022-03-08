# Climbing Stairs problem
* You are climbing a staircase. It takes `n` steps to reach the top.
* Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

Leetcode link: https://leetcode.com/problems/climbing-stairs/

<br />

### Approach 1: Brute Force, climbStairsRecursion()
This is a brute force solution where we consider all possible paths that we can take to get to the top. At each step, we can either climb 1 step or 2 steps, if we've reach the top, increment the result counter and explore the next possible path.

```python3
# exhaust all possible paths
def climbStairsRecursion(self, n: int) -> int:
    return self.helper(0, n)

def helperRecursion(self, cur, n):
    result = 0
    if cur == n:
        result = 1
    else:
        if cur+1 <= n:
            result += self.helperRecursion(cur+1, n)

        if cur+2 <= n:
            result += self.helperRecursion(cur+2, n)
    return result
```

This solution leads to TLE :(, not surprisingly

<br />

### Approach 2: Fibonacci, Recursion, climbStairsMath()
This solution is based on the calculation of fibonacci series. Because each value is equal to the sum of previous two values, we can use recursion with memorization to calculate the final result.


```python3
# similar to fibonacci series, use recursion with memorization to calculate 
def climbStairsMath(self, n: int) -> int:
    cache = {}
    return self.helperMath(n, cache)

def helperMath(self, n, cache):
    if n<=3:
        result = n
    else:
        if n-1 not in cache.keys():
            a = self.helperMath(n-1, cache)
            cache[n-1] = a

        if n-2 not in cache.keys():
            b = self.helperMath(n-2, cache)
            cache[n-2] = b

        result = cache[n-1] + cache[n-2]

    return result
``

Actual running time:\
![d2b2ae0820e71112812efd5c2220019](https://user-images.githubusercontent.com/25105806/130372380-a4d89d2c-9dd7-4a52-989c-b3fd97659c46.png)

<br />

### Approach 3: Fibonacci, Iteration1, climbStairsIteration1()
Instead of using recursion to calculate Fibonacci, we can also use iteration to calcualte. This approach stores all calculated values in the list.

```python3
# use iteration to calculate, store all seen values in a list
def climbStairsIteration1(self, n: int) -> int:
    if n<=3:
        return n
    else:
        result = [1,2,3]
        for _ in range(n-3):
            result.append(result[-1] + result[-2])
    return result[-1]
```

Actual running time:\
![c4cd90fa4eeb4d263b15558b8fd162a](https://user-images.githubusercontent.com/25105806/130372424-5832ee65-b7ee-4998-abdb-aa55b8b243c5.png)

<br />

### Approach 4: Fibonacci, Iteration2, climbStairsIteration2()
It is not hard to find out that the only two values matter are the immediate previous two values, all values in the past need not to be stored, so we can only use two variables `a` and `b` to store the previous two values and exchange value when calculating new value.

```python3
# use iteration to calculate, only keeping two variables
def climbStairsIteration2(self, n: int) -> int:
    if n<=3:
        return n
    else:
        a, b = 2, 3
        for _ in range(n-3):
            c = a + b
            a = b
            b = c
    return b
```

Actual running time:\
![bba600022cd328a5b254c5bb614d8bd](https://user-images.githubusercontent.com/25105806/130372457-386eeb77-6335-44f0-b524-e10b989b1932.png)

