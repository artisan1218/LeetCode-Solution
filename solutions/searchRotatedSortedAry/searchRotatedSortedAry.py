from typing import List

class Solution:
    '''
    Binary Search solution 1 with recursion
    '''
    def searchBinarySearch1(self, nums: List[int], target: int) -> int:
        # first to find the pivot index
        pivot = self.binarySearchPivot(nums, 0)
        pivot = len(nums)-1 if pivot==-1 else pivot
        # then find the target according to pivot index
        idx = self.binarySearchTarget(nums, target, pivot)
        return idx

    def binarySearchTarget(self, nums: List[int], target: int, pivot: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        else:
            # decide which side of pivot does the target locate
            if nums[0] < target:
                # target is in the left side of pivot
                left = 1
                right = pivot+1
            elif nums[0] > target:
                # target is in the right side of the pivot
                left = pivot
                right = len(nums)
            else:
                # nums[0] == target
                return 0
            
            # binary search the target
            while left!=right:
                checkPt = int((left + right)/2)
                if nums[checkPt]<target:
                    left = checkPt+1
                elif nums[checkPt]>target:
                    right = checkPt
                else:
                    return checkPt
            return -1
        
    def binarySearchPivot(self, nums: List[int], totalIndex: int) -> int:
        # the -1 here simply means we cannot find the pivot point in this subarray
        if len(nums)==1:
            return -1
        else:
            # index where we partition the list into two parts to perform binary search
            checkPt = int(len(nums) / 2)
            if checkPt+1 < len(nums) and nums[checkPt] > nums[checkPt+1]:
                return checkPt + totalIndex
            elif checkPt-1 >=0 and nums[checkPt] < nums[checkPt-1]:
                return checkPt - 1 + totalIndex
            else:
                # totalIndex is to calculate the index of the pivot point in entire list not just this subarray
                leftSideIdx = self.binarySearchPivot(nums[0:checkPt], totalIndex)
                rightSideIdx = self.binarySearchPivot(nums[checkPt:], totalIndex+checkPt)
                # the partition without pivot point will always have a result of -1
                return max(leftSideIdx, rightSideIdx)
    
    '''
    Binary Search solution 2 
    '''
    def searchBinarySearch2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        # use binary search to find the pivot point
        while left<right:
            midpoint = int((left + right)/2)
            if nums[midpoint] > nums[right]:
                # the midpoint value is larger than the right value
                # so this is the subarray where rotation happens
                # move the left pointer up the point where midpoint
                # value is not longer greater than right value
                left = midpoint+1
            else:
                # if midpoint value is smaller than the right value
                # then this means the subarray bounded by left and right
                # is sorted, so we should move right pointer to the midpoint
                # to check the other half of the array
                right = midpoint
        
        # left and right pointer will finally meet at the same point
        # this is where begin our next binary search to find the target
        pivot = left
        left = 0
        right = len(nums)-1
        
        # first to decide which part of the array should we perform bianry search on
        if target>=nums[pivot] and target<=nums[right]:
            # the right part of the array
            left = pivot
        else:
            # the left part of the array
            right = pivot
        
        # this is where regular binary search begins
        while left<=right:
            midpoint = int((left+right)/2)
            if nums[midpoint]<target:
                left = midpoint+1
            elif nums[midpoint]>target:
                right = midpoint-1
            else:
                return midpoint
        return -1
                
    
if __name__ == "__main__":
    solver = Solution()
    nums = [1,3]
    target = 3
    print(solver.searchBinarySearch2(nums, target))





