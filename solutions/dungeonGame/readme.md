# Dungeon Game problem
![image](https://user-images.githubusercontent.com/25105806/226208838-40d1e298-bf12-482f-b85a-8fd045ca9d04.png)


Leetcode link: https://leetcode.com/problems/dungeon-game/

<br />

### Approach 1: DFS, calculateMinimumHP()

The idea is to use DFS to search every possible ways exhausitively, the record the minimum HP required to get to princess. This solution leads to TLE because the complexity is just too high.

```python3
def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
	def helper(dungeon, x, y, minHP, curHP):
		if x<len(dungeon) and y<len(dungeon[x]):
			# reached the bottom-right corner
			if x==len(dungeon)-1 and y==len(dungeon[x])-1:
				curHP += dungeon[x][y]
				minHP = min(minHP, curHP)
				self.result = max(self.result, minHP)
			else:
				curHP += dungeon[x][y]
				minHP = min(minHP, curHP)
				if curHP < self.result:
					return
				helper(dungeon, x, y+1, minHP, curHP) # rightward
				helper(dungeon, x+1, y, minHP, curHP) # downward

	self.result = float('-inf')
	helper(dungeon, 0, 0, 0, 0)
	return abs(self.result)+1
```

<br />

### Approach 2: DP, calculateMinimumHPDP()

Credits to: https://www.youtube.com/watch?v=xdFzPCa9g4A

If regular DFS leads to TLE, then it means there must be some ways to speed this up like memorization. A common way of thinking is to use a 2-d dp array where each cell represents the minimum HP required to get from upper-left corner to current cell. But since we're not only caring about the minimum HP at the final cell, but also making sure HP does not fall below zero at any given cell along the path. So if we start at the upper-left corner and work our way down to destination, we have to maintain an extra piece of information, namely currentHP and minimumHP, which will the dp array 3-d instead of 2-d. This is just too complicated and hard to validate. So instead of top-down, we can try bottom-up approach, where we start at the bottom-right corner and work our way up to the begining point. 

In the 2-d array, each cell still represents the minimum HP required to get to princess from current cell. So the minHP required at the destination cell is just `1-dungeon[-1][-1]`. Note that since we want to keep it minimum, which means if `dungeon[-1][-1]` is positive, we actually do not need to have any more HP than 1, so we can set a max limit of HP at 1.

Then for each cell in the middle(not on the edge), there are two possible ways to get here, either from top(go down) or left(go right), so we want to get the minimum HP of these two ways. Thus the dp formula for each cell is 

```python3
right = max(dp[x][y+1] - dungeon[x][y], 1)
down = max(dp[x+1][y] - dungeon[x][y], 1)
dp[x][y] = min(right, down)
```

Full code:
```python3
def calculateMinimumHPDP(self, dungeon: List[List[int]]) -> int:
	# dp[x][y] = minimum HP needed at this cell to get to princess
	# we trace back from princess to starting point
	dp = [[0 for i in range(len(dungeon[0]))] for i in range(len(dungeon))]
	dp[-1][-1] = max(1 - dungeon[-1][-1], 1)

	# since we can only go rightward or downward, when tracing back, we can only go leftward or upward
	# fill in last row from right to left
	for y in range(len(dungeon[-1])-2, -1, -1):
		dp[-1][y] = max(dp[-1][y+1] - dungeon[-1][y], 1)

	# fill in last column from bottom to top
	for x in range(len(dungeon)-2, -1, -1):
		dp[x][-1] = max(dp[x+1][-1] - dungeon[x][-1], 1)

	# dp
	for x in range(len(dungeon)-2, -1, -1):
		for y in range(len(dungeon[x])-2, -1, -1):
			right = max(dp[x][y+1] - dungeon[x][y], 1)
			down = max(dp[x+1][y] - dungeon[x][y], 1)
			dp[x][y] = min(right, down)

	return dp[0][0]
```


Time complexity is O(m*n) where m and n are height and width of the dungeon map:

![image](https://user-images.githubusercontent.com/25105806/226210554-98872a12-c900-4cf9-ad23-ce555c8f3e90.png)
