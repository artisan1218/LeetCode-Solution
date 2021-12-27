# Sentence Screen Fitting problem
<img width="1043" alt="image" src="https://user-images.githubusercontent.com/25105806/138172398-8d10fdb1-d5cc-4007-be70-01ba0e52f04d.png">

Leetcode link: https://leetcode.com/problems/sentence-screen-fitting/

<br />

### Approach 1: Brute Force, wordsTypingBruteForce()
The brute force solution simply go over the list `sentence` word by word and check if the current line still fit in the current word. This solution leads to TLE.

```python
def wordsTypingBruteForce(self, sentence: List[str], rows: int, cols: int) -> int:
    wordIdx = 0
    result = 0
    for row in range(rows):
        usedCol = 0
        while (usedCol + len(sentence[wordIdx])) <= cols:
            usedCol += len(sentence[wordIdx]) + 1
            wordIdx += 1
            if wordIdx == len(sentence):
                result += 1
                wordIdx = 0
    return result
```

Time complexity is O(n) where n is the length of `sentence`


<br />

### Approach 2: wordsTyping()
A better solution is to add the whole line one time instead of add word by word. This way we can reduce the time of iteration to the number of `rows`. Then we check if the ending char in each line is am empty space ` `. If it's an empty space, then we are good because that means we fit the whole line in without cutting any word in half. If it's not empty space, we should iteratively go back until we've met a empty space, this way to can avoid cutting any word in half.

```python
def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    sentenceStr = ' '.join(sentence) + ' '
    pos = 0
    l = len(sentenceStr)
    for _ in range(rows):
        pos += cols
        if sentenceStr[pos%l]==' ':
            # we're good
            pos += 1 # skip the space
        else:
            while pos>0 and sentenceStr[(pos-1)%l]!=' ':
                pos-=1
    return pos//l
```

Time complexity is O(rows):\
<img width="728" alt="image" src="https://user-images.githubusercontent.com/25105806/138173505-5b5c387e-c561-4dd4-a38b-cf29f60ac32d.png">


