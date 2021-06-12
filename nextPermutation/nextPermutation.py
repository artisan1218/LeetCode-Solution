
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        # find the first number that is smaller than next number, going left from right-most index
        # largest index i such that a[i] < a[i + 1]
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i==-1:
            nums.reverse()
        else:
            # find the first number that is greater than nums[i], going left from right-most index
            # largest index j greater than i such that a[i] < a[j].
            j = len(nums) - 1
            while j>i and nums[j] <= nums[i]:
                j-=1
            # Swap the value of i with that of j.
            nums[i], nums[j] = nums[j], nums[i]
          
            # Reverse the sequence from a[i + 1] up to and including the final element a[n].
            nums[i+1:] = nums[i+1:][::-1]
        return


if __name__ == "__main__":
    solver = Solution()
    nums = [5, 1, 1]
    solver.nextPermutation(nums)
    print(nums)






