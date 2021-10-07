# Number of Good Ways to Split a String problem
![image](https://user-images.githubusercontent.com/25105806/136476432-4e973f6e-e04c-4e82-a925-292ca7052176.png)

Leetcode link: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

<br />

### Approach 1: Brute Force, numSplitsBruteForce()
The idea is simple, we cut the string `s` into two parts and check for the number of unique characters in each part `p` and `q`.

```python
def numSplitsBruteForce(self, s: str) -> int:
    def isGoodWay(p, q):
        return len(set(p)) == len(set(q))

    count = 0
    for i in range(1, len(s)):
        print(s[0:i], s[i:])
        if isGoodWay(s[0:i], s[i:]):
            count+=1
    return count
```

Time complexity is O(n^3), iteration over the string is O(n), string slicing is O(n) and checking for unique characters is also O(n):\
This solution leads to TLE

<br />

### Approach 2: Cache, numSplitsCache1()
The idea is to use two dict and two sets to store the number of unique characters from left and from right. `i` is the index of `s` and the corresponding value stands for the number of unique characters up to index `i`. 

```python
def numSplitsCache1(self, s: str) -> int:
    leftUnique = dict()    
    rightUnique = dict()    
    leftSeen = set()
    rightSeen = set()
    sLen = len(s)
    for i in range(0, len(s)):
        if s[i] not in leftSeen:
            leftSeen.add(s[i])
            leftUnique[i] = leftUnique.get(i-1, 0) + 1
        else:
            leftUnique[i] = leftUnique[i-1]

        if s[sLen-i-1] not in rightSeen:
            rightSeen.add(s[sLen-i-1])
            rightUnique[sLen-i-1] = rightUnique.get(sLen-i, 0) + 1
        else:
            rightUnique[sLen-i-1] = rightUnique[sLen-i]

    count = 0
    for i in range(0, len(s)-1):
        if leftUnique[i] == rightUnique[i+1]:
            count+=1

    return count
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136476814-1b0c295b-bede-4537-b797-feed7db37dd5.png)

<br />

### Approach 3: Cache, numSplitsCache2()
Same idea, but uses two list instead of two dict to store the number of unique characters at index `i`

```python
def numSplitsCache2(self, s: str) -> int:
    leftUnique = list()    
    rightUnique = list()    
    leftSeen = set()
    rightSeen = set()
    sLen = len(s)
    for i in range(0, len(s)):
        leftSeen.add(s[i])
        rightSeen.add(s[sLen-i-1])
        leftUnique.append(len(leftSeen))
        rightUnique.append(len(rightSeen))

    count = 0
    for i in range(0, len(s)-1):
        if leftUnique[i] == rightUnique[sLen-i-2]:
            count+=1

    return count
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136476912-22e180a2-2676-41a8-a937-a046d37fb61d.png)

