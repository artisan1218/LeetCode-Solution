from typing import List

class Solution:
    def removeElementTwoPointers(self, nums: List[int], val: int) -> int:
        modifier = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[modifier] = nums[idx]
                modifier+=1
        return modifier
    
    def removeElementBuiltinFunc(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    solver = Solution()
    inputList = [1,1,2,3,4,5,5,6]
    val = 1
    result = solver.removeElementBuiltinFunc(inputList, val)
    print("length is: ", result)
    print(inputList)



