# %%
def inversion(arr):
    count = 0
    def helper(uniqueArr, curLen, idx, prevNum):
        nonlocal count
        if curLen == 3:
            count += 1
        else:
            for i in range(idx, len(uniqueArr)):
                if curLen==0 or uniqueArr[i] < prevNum:
                    helper(uniqueArr, curLen + 1, i + 1, uniqueArr[i])

    seen = set()
    uniqueArr = list()
    for num in arr:
        if num not in seen:
            seen.add(num)
            uniqueArr.append(num)

    helper(uniqueArr, 0, 0, 0)
    return count

arr = [5, 3, 4, 2, 1]
result = inversion(arr)
print(result)

# %%
def inversion2(arr):
    def helper (arr, curSeq, idx):
        if len(curSeq)== 3:
            result.append(curSeq)
        else:
            for i in range(idx, len(arr)) :
                if len(curSeq)==0 or arr[i] < curSeq[-1]:
                    helper(arr, curSeq+[arr[i]], i + 1)

    result = list()
    seen = set()
    uniqueArr = list()
    for num in arr:
        if num not in seen:
            seen.add(num)
            uniqueArr.append(num)

    helper (uniqueArr, [], 0)
    return result

arr = [5, 3, 4, 2, 1]
result = inversion2(arr)
print(result)

# %%
def inversion3(arr):
    greater = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                greater[i] += 1
    # count for each elements in the arr, how many element on the right are smaller than it
    # this number is simply the count of size-2-inversions for each number

    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                # if arr[i] > arr[j], we can make a size-3-inversion by connecting arr[i].
                # we only care about the count, then simply add up the count for size-2-inversions
                # this works because for size-3-inversions starting with a specific number, its counts 
                # are simply the sum of all size-2-inversions that are smaller than that number
                result += greater[j]

    return result

arr = [5, 3, 4, 2, 1]
result = inversion3(arr)
print(result)

# %%
def inversion4(arr):
    result = 0    
    for mid in range(1, len(arr)):
        smaller = 0
        for right in range(mid+1, len(arr)):
            if arr[mid] > arr[right]:
                smaller += 1
        
        greater = 0
        for left in range(0, mid):
            if arr[left] > arr[mid]:
                greater += 1
        
        result += smaller * greater

    return result

arr = [5, 3, 4, 2, 1]
inversion4(arr)


