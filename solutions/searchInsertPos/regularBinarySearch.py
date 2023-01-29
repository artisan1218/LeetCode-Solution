
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        # regular binary search
        while left<=right:
            midpoint = int((left+right)/2)
            if nums[midpoint] < target:
                left = midpoint+1
            elif nums[midpoint] > target:
                right = midpoint-1
            else:
                return midpoint
        
        # if not found, the index where left and right meet will be the place for insertion
        return left
    

if __name__ == "__main__":
    solver = Solution()
    nums = [1,3,5,6]
    target = 4
    print(solver.searchInsert(nums, target))





