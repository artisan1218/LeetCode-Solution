#!/usr/bin/env python
# coding: utf-8

# In[12]:


#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#

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


if __name__ == '__main__':
    grid1 = [[1,1,1],[1,0,0],[1,0,0]]
    grid2 = [[1,1,1],[1,0,0],[1,0,1]]
    print(countMatches(grid1, grid2))


# In[ ]:




