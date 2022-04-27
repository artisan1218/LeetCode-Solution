# Image Matching problem
* Images are stored in the form of a grid. Image recognition is possible by comparing grids of two images and checking if they have any matching regions.
* You are given two grids where each cell of a grid contains is either 0 or 1. If two cells share a side then they are adjacent. Cells that contain 1s form a connected region if any cell of that region can be reached by moving through the adjacent cells that contain 1. Overlay the first grid onto the second and if a region in the first grid completely matches a region in the second grid, the regions are matched.
* Count total number of such matched regions in the second grid.
* For example given two 3x3 grids:
```
G1:	111		G2: 111
	100		    100
	100		    101
```
* There are two regions in G2: {(0,0), (0,1), (0,2), (1,0), (2,0)} and {(2,2)}. Regions in G1 cover the first region in G2 but not the second region. Thus, there is only one matching region.

### Approach 1: Connected Components, countMatches()
The idea is to count the connected components in both `grid1` and `grid2`, then compare all the connected components, if they are same, increment counter by 1.\
The key is to use stack to calculate all connected component 
```
stack.append((row, col-1))
stack.append((row-1, col))
stack.append((row+1, col))
stack.append((row, col+1))
```
Popping each of the (row,col) pair and check if it is a `1` and append all its surrounding cells to the stack, until we've popped all cells out of stack.


```python3
def region(grid, visited, i, j):
    numRow = len(grid)
    numCol = len(grid[0])
    
    regionList = []
    stack = [(i, j)]
    # if the stack is empty, then it means we've explored all adjacent cell around (i, j)
    while len(stack)!=0:
        # pop a cell out to check if it's a valid adjacent cell
        row, col = stack.pop()
        # if row or col is not within the matrix, we can discard it
        if 0<=row and row <numRow and 0<=col and col<numCol and (row, col) not in visited:
            # if the current cell is 1, we should add it to the region list because it is connected
            # then we should expand the surrounding four cells, to check adjacent cells around it
            # then add current cell to visited to avoid double checking
            if grid[row][col] == 1:
                # this is a valid adjacent cell, we append this cell to region list
                regionList.append((row, col))
                # keep exploring all four directions
                stack.append((row, col-1))
                stack.append((row-1, col))
                stack.append((row+1, col))
                stack.append((row, col+1))
            # we've explored this coord
            visited.add((row, col))
    return regionList

def regions(grid, visited):
    foundRegions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # 1 is not int but string
            if grid[i][j]==1 and (i, j) not in visited:
                #given current coord, found the connected regions
                foundRegion = region(grid, visited, i, j)
                foundRegions.append(foundRegion)

    return foundRegions

def countMatches(grid1, grid2):
    
    # found all regions in grid1 and grid2
    # set() is used to avoid double checking same cell
    grid1Region = regions(grid1, set())
    grid2Region = regions(grid2, set())
    
    count = 0
    for r1 in grid1Region:
        for r2 in grid2Region:
            # if the found region is same, then increment counter by 1
            if r1==r2:
                count+=1
    return count

```
