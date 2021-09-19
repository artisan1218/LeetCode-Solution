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
