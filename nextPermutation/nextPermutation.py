
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        # Find the largest index i such that nums[i] < nums[i + 1]. 
        # If no such index exists, just reverse nums and we are done.
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i==-1:
            nums.reverse()
        else:
            # Find the largest index j > i such that nums[i] <= nums[j].
            j = len(nums) - 1
            while j>i and nums[j] <= nums[i]:
                j-=1
            # Swap the value of i with that of j.
            nums[i], nums[j] = nums[j], nums[i]
          
            # Reverse the sub-array nums[i + 1:].
            nums[i+1:] = nums[i+1:][::-1]
        return


if __name__ == "__main__":
    solver = Solution()
    nums = [5, 1, 1]
    solver.nextPermutation(nums)
    print(nums)


