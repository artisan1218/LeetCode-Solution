# Minimum Difference Between Largest and Smallest Value in Three Moves problem
![image](https://user-images.githubusercontent.com/25105806/136305954-cfdb7231-924b-42fe-ae08-247e91ea3dcb.png)

Leetcode link: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

<br />

### Approach 1: Brute Force, minDifferenceBruteForce()
The idea is to first sort the list in ascending order. Since we only remove 3 elements to make the difference smallest, we have to remove either smallest elements or biggest elements. We then try all four different possibilities of removing:\
1. Removing 3 smallest elements
2. Removing 3 biggest elements
3. Removing 2 smallest and 1 biggest
4. Removing 1 smallest and 2 biggest

Then simply return the smallest one.


```python
def minDifferenceBruteForce(self, nums: List[int]) -> int:
    if len(nums)>4:
        left = 0
        right = len(nums)-1
        nums.sort()

        lll = nums[right] - nums[left+3] # cut 3 smallest elements
        rrr = nums[right-3] - nums[left] # cut 3 biggest elements
        llr = nums[right-1] - nums[left+2] # cut 2 smallest and 1 biggest
        lrr = nums[right-2] - nums[left+1] # cut 1 smallest and 2 biggest

        return min(lll, rrr, llr, lrr)
    else:
        return 0
```

Time complexity is O(nlogn) because of the sorting:
![image](https://user-images.githubusercontent.com/25105806/136305839-5921d98e-1de1-4111-8df9-de4fa5c45f27.png)

<br />

### Approach 2: Backtracking, minDifferenceBacktrack()
Instead of manually list all four possibilities, we use backtrack to explore. At each stage, we can either remove the smallest(left-most) one or biggest(right-most) one. By using backtracking we can adapt different number of removing instead of just 3.

```python
def minDifferenceBacktrack(self, nums: List[int]) -> int:
    def backtrack(nums, remainingNum, left, right):
        if remainingNum!=0:
            cutFromLeft = backtrack(nums, remainingNum-1, left+1, right)
            cutFromRight = backtrack(nums, remainingNum-1, left, right-1)
            return min(cutFromLeft, cutFromRight)
        else:
            return nums[right]-nums[left]

    if len(nums)>4:
        nums.sort()
        return backtrack(nums, 3, 0, len(nums)-1)
    else:
        return 0
```

Time complexity is O(nlogn):\
![image](https://user-images.githubusercontent.com/25105806/136306135-1dbdbd39-57bb-4985-955e-fb03013b27ad.png)

