# Number of Matching Subsequences problem
![image](https://user-images.githubusercontent.com/25105806/136671888-7a70bc42-8d4a-446f-9b7f-4d4fd6350735.png)

Leetcode link: https://leetcode.com/problems/number-of-matching-subsequences/

<br />

### Approach 1: Brute Force, numMatchingSubseqBruteForce()
The idea is to use a dict to count the number of occurrences for each word in `words` so that we don't have to recount them for many times. Then simply go over each word in the dict to see if they are a subsequence of `s`

```python
def numMatchingSubseqBruteForce(self, s: str, words: List[str]) -> int:
    def match(subsq, s):
        j = 0
        for i in range(len(s)):
            if s[i] == subseq[j]:
                j+=1
            if j==len(subseq):
                return True
        return False

    count = dict()
    for subseq in words:
        count[subseq] = count.get(subseq, 0) + 1

    result = 0
    for subseq in count:
        if match(subseq, s):
            result+=count[subseq]
    return result
```

Time complexity is O(m\*n) where m is the number of unique words in `words` and n is the length of `s`:\
![image](https://user-images.githubusercontent.com/25105806/136671972-564cf72b-8d7f-4dc2-9ce3-673160fa6381.png)

<br />

### Approach 2: Binary Search, numMatchingSubseqBinarySearch()
Credits to: https://www.youtube.com/watch?v=9zzDQJLcY9Y

We can first go over `s` to get the index of each char of `s`. Then iterate through each word in `words`, check if each char in word is also in the dict and in same order using binary search. 

```python
def numMatchingSubseqBinarySearch(self, s: str, words: List[str]) -> int:
    def binarySearch(lst, tgt):
        l = 0
        r = len(lst)
        while l<r:
            mid = (l+r)//2
            if lst[mid] > tgt:
                r = mid
            else:
                l = mid + 1
        return l

    lookup = defaultdict(list)
    for idx, char in enumerate(s):
        lookup[char].append(idx)

    result = 0
    for word in words:
        start = -1
        found = True
        for char in word:
            tgtIdx = binarySearch(lookup[char], start)
            if tgtIdx == len(lookup[char]):
                found = False
                break
            else:
                start = lookup[char][tgtIdx]
        if found:
            result+=1
    return result
```

Time complexity is O(n\*m\*logm) where n is the length of `s` and m is the length of `words`:
![image](https://user-images.githubusercontent.com/25105806/136672067-116d4fc0-1ba5-46af-aa95-78bb07b6e4e0.png)


<br />

### Approach 3: Next Pointer, numMatchingSubseqNextPointer()
![image](https://user-images.githubusercontent.com/25105806/136672110-a6d715d7-fc72-47c4-b3be-2a8b555e29c8.png)

```python3
def numMatchingSubseqNextPointer(self, s: str, words: List[str]) -> int:
    pointerDict = defaultdict(list)
    for word in words:
        pointerDict[word[0]].append(word[1:])

    result = 0    
    for char in s:
        waitingList = pointerDict[char]
        pointerDict[char] = []
        for suffix in waitingList:
            if len(suffix)==0: # we have reached the end of current word
                result += 1
            else:
                # update the dict with new char and its suffix
                pointerDict[suffix[0]].append(suffix[1:])
    return result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/136672164-94fe34da-b27e-4a40-9749-070db2c22eff.png)

