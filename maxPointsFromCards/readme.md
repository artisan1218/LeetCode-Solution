# Maximum Points You Can Obtain from Cards problem
![image](https://user-images.githubusercontent.com/25105806/136644172-3a76d1cb-f373-4a34-96bd-092b6b112fc1.png)

Leetcode link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

<br />

### Approach 1: DFS, maxScoreDFS()
Use DFS to explore all possible ways of obtaining cards from either side.\
This solution leads to TLE

```python
def maxScoreDFS(self, cardPoints: List[int], k: int) -> int:
    def dfs(cardPoints, k, l, r):
        if k==0:
            return 0
        else:
            left = cardPoints[l] + dfs(cardPoints, k-1, l+1, r) # take from left
            right = cardPoints[r] + dfs(cardPoints, k-1, l, r-1) # take from right
            return max(left, right)

    return dfs(cardPoints, k, 0, len(cardPoints)-1)
```

Time complexity is O(2^k) since we have to consider two cases k times


<br />

### Approach 2: Iteration, maxScoreIteration()
Since the total number of cards we obtain is always `k`, we can iteratively consider all cases for left and right. List slicing is probably the reason this solution is too slow. \
This solution leads to TLE

```python
def maxScoreIteration(self, cardPoints: List[int], k: int) -> int:
    result = 0
    for leftNum in range(k+1):
        rightNum = k-leftNum
        result = max(result, sum(cardPoints[:leftNum])+sum(cardPoints[len(cardPoints)-rightNum:]))

    return result
```

Time complexity is O(n\*k) since we have to slice the list for k times

<br />

### Approach 3: Iteration2, maxScoreIteration2()
Instead of slicing the list in each iteration, we can build two list to store the sum of value at index `i`. `l2r` stores the sum of value from left to right and `r2l` records the sum of value from right to left. Then simply get the value in both list in O(1) time in a loop to obtain the max value. 

```python
def maxScoreIteration2(self, cardPoints: List[int], k: int) -> int:
    l2r = [0]
    r2l = [sum(cardPoints)]
    for idx, point in enumerate(cardPoints):
        l2r.append(l2r[-1] + point)
        r2l.append(r2l[-1] - point)

    result = 0
    for leftNum in range(k+1):
        rightNum = k-leftNum
        result = max(result, l2r[leftNum]+r2l[len(cardPoints)-rightNum])

    return result
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136644395-52bc48b5-813d-459a-87d9-4262013991ce.png)

<br />

### Approach 4: Sliding Window, maxScoreSlidingWindow()
Credits to: https://www.youtube.com/watch?v=TsA4vbtfCvo

We can use two pointers `left` and `right` to mark the boundry of a sliding window. We want the sum of values that are outside of the sliding window and compare them for the max value. We first set the sliding window at the left most position by setting `left=0` and `right=len(cardPoints)-k`. Then we calculate the sum of remaining values using O(n) time. Then we enter the loop and update the value by subtracting right-most value of the sliding window and adding left-most value of the sliding window, this simulates the action of move the window to right by one position. This will only require O(1) time and we do this in a loop for `k` times.

```python
def maxScoreSlidingWindow(self, cardPoints: List[int], k: int) -> int:
    left = 0
    right = len(cardPoints)-k
    result = sum(cardPoints[right:])
    curSum = sum(cardPoints[right:])

    for _ in range(k):
        # move the sliding window to right by one pos
        curSum = curSum - cardPoints[right] + cardPoints[left]
        result = max(result, curSum)
        left+=1
        right+=1
    return result
```

Time complexity is O(k):\
![image](https://user-images.githubusercontent.com/25105806/136644559-101f1024-0318-4422-a143-86355d2313fa.png)

