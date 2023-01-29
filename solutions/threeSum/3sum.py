from typing import List

'''Approach 1'''
# use nested loop to go through each 3-tuple combination of the numbers and check if they add up to 0
def threeSumBruteForce(nums: List[int]) -> List[List[int]]:
    result = set()
    if len(nums)<3:
        return []
    else:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                for idx3, num3 in enumerate(nums):
                    if idx1!=idx2 and idx1!=idx3 and idx2!=idx3 and num1+num2+num3==0:
                        uniqueList = tuple(sorted(tuple((num1, num2, num3))))
                        result.add(uniqueList)
        return [list(t) for t in result]
    


'''Approach 2'''
# use a O(n^2) algorithm first to generate all possible sums of two numbers and store them in a dict
# then go through the number list again to retrieve the desired sum using O(n) time
def generateAllTwoSums(nums):
    seenAns = dict()
    sum2IndicesDict = dict()
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if 0-num1-num2 in nums:
                if idx1!=idx2:
                    if num1+num2 in sum2IndicesDict:
                        sum2IndicesDict[num1+num2].append((idx1, idx2))
                    else:
                        sum2IndicesDict[num1+num2] = [(idx1, idx2)]
               
    return sum2IndicesDict

def threeSum2(nums: List[int]) -> List[List[int]]:
    sum2IndicesDict = generateAllTwoSums(nums)
    result = set()
    for idx, num in enumerate(nums):
        num2IndicesList = sum2IndicesDict.get(0-num, [])
        if num2IndicesList:
            for indicesTuple in num2IndicesList:
                if idx!=indicesTuple[0] and idx!=indicesTuple[1]:
                    result.add(tuple(sorted([nums[indicesTuple[0]], nums[indicesTuple[1]], num])))
    return [list(t) for t in result]


'''Approach 3'''
# the idea is similar to approach 2, go through the list once and generate the desired twoSum value using O(n) time
# the total time complexity is therefore O(n^2)
def threeSumHash(nums: List[int]) -> List[List[int]]:
    result = set()
    for idx, num in enumerate(nums):
        twoSumList = twoSumHash(nums, 0-num)
        for twoSum in twoSumList:
            if idx!=twoSum[0][1] and idx!=twoSum[1][1]:
                threeSum = tuple(sorted([twoSum[0][0], twoSum[1][0], num]))
                result.add(threeSum)

    return [list(t) for t in result]
    
    
def twoSumHash(nums, targetTwoSum):
    seenAns = set()
    resultList = list()
    mapper = dict()
    for idx, num in enumerate(nums):
        num1 = num
        num2 = targetTwoSum-num1
        if num2 not in mapper:
            mapper[num] = idx
        else:
            if num1 not in seenAns and num2 not in seenAns:
                resultList.append([(num1, idx), (num2, mapper[num2])])
                seenAns.add(num1)
                seenAns.add(num2)
    return resultList

'''Approach 4'''
def threeSumOptimal(nums: List[int]) -> List[List[int]]:
    result = list()
    nums.sort()
    # at least three elements in nums is needed, otherwise just return empty list
    for idx in range(len(nums)-2):
        # use two pointers to bound the range
        left = idx+1 # left pointer always start at current index + 1 so that it never visit seen elements
        right = len(nums)-1
        # if current idx=0, then there is no element before it, so no need to check
        # if current idx is not 0, then check if the element before it is same as current element, if is, skip
        if nums[idx]>0:
            # if the current value, which is also the left-most value, is greater than 0, 
            # then the remaining number must be greater than 0 as well, 
            # so there is no need to check the sum because sum of positives cannot be 0
            break
        else:
            if idx==0 or nums[idx]!=nums[idx-1]:
                while left < right:
                    # similarly, if the right-most value, which is the greatest value, is smaller than 0, 
                    # then the sum cannot be 0 as well because sum of negatives cannot be 0
                    if nums[right] < 0:
                        break
                    else:
                        if nums[idx] + nums[left] + nums[right] == 0:
                            result.append([nums[idx], nums[left], nums[right]])
                            while left<right and nums[left]==nums[left+1]: # skip duplicate elements
                                left+=1
                            while left<right and nums[right]==nums[right-1]: # skip duplicates
                                right-=1
                            left+=1 # move the left pointer to a new pos
                            right-=1 # move the right pointer to a new pos
                        elif nums[idx] + nums[left] + nums[right] < 0:
                            left+=1
                        else:
                            right-=1
    return result

if __name__ == "__main__":
    l = [-1,0,1,2,-1,-4]
    print(threeSumOptimal(l))







