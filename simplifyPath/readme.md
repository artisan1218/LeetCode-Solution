# Spiral Matrix problem
* Given an `m` x `n` matrix, return all elements of the `matrix` in spiral order.
  
  ![image](https://user-images.githubusercontent.com/25105806/127098278-7fdc9cb1-9465-4e16-9982-1f9732f2552e.png)


### Approach 1: List Traversal, spiralOrder()
The idea is very straight-forward, we will read in the `matrix` in spiral order. That is, read first line from left to right, then top to bottom, right to left, then bottom to top, then start another loop of reading in this order until we've read all elements in the matrix.

The time complexity is O(n) because we will reach each element in the matrix exactly once
![image](https://user-images.githubusercontent.com/25105806/127098523-a541c29c-cb91-4f77-8741-504a8f325374.png)
