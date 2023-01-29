# Substring with Concatenation of All Words problem
* You are given a string `s` and an array of strings `words` of the **same length**. Return all starting indices of substring(s) in `s` that is a concatenation of each `word` in words exactly once, in any order, and without any intervening characters.

You can return the answer in **any order**.

Leetcode link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

<br />

### Approach 1: Brute Force, findSubstringBruteForce()
This approach is the naive approach that we slide through the input string `s` and get each word of the same length as word in `words`, then check if this word is in `words`. If not, then check the next word, if the word is in the list, then iteratively check them one by one.

```python3
def findSubstringBruteForce(self, s: str, words: List[str]) -> List[int]:
    result = []
    wordLen = len(words[0])
    for strPtr in range(len(s)-wordLen+1):
        # window is the substring bounded by strPointer with the same length as word in words
        window = s[strPtr:strPtr + wordLen]
        # used to move the strPtr without modifying it
        strPtrMover = 0
        tmpWords = words.copy()
        while window in tmpWords:   
            tmpWords.remove(window)              
            strPtrMover += 1
            # get the next window word in s
            window = s[strPtr + wordLen * strPtrMover: strPtr + wordLen * (strPtrMover+1)]

        # wordPointer walked all the way to the end of words list, which means every word in the list has been found in s
        if len(tmpWords)==0:
            result.append(strPtr)

    return result
```

Time complexity is O(mn^2) because we will go through each char in string `s`, which is O(m), and check each word in `words`, which is O(n), and keep a copy of the `words` because of the line ```tmpWords = words.copy()```, which is also O(n). \
Actual running time is indeed quite slow:\
![image](https://user-images.githubusercontent.com/25105806/121616947-c484de80-ca18-11eb-991f-e1d879f5dad5.png)

This approach can be improved in many ways:
1. We don't need to keep a copy of `words` everytime we check substring, just use map structure for comparsion
2. Add early termination conditions. For example when we've checked same number of words as all number of words in the list `words`, and when a specific word has appeared more than that many times in `words`.
3. When a word does not exist in the `words`, we can directly jump to the next char of that non-existing word because any substring before that non-existing word is not going to be valid substring.

<br />

### Approach 2: Two Maps, findSubstringTwoMaps()
Credits to https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13658/Easy-Two-Map-Solution-(C++Java)


We use two maps in this approach for comparsion. Since the order of words does not matter. We only need to keep track of each word and its frequency. The first map `count` is used to keep track of how many words appeared in list `words` for how many times. The second map `current` is used to keep track of seen words so far. We can then simply compare the number of words in `words` and the number of words in `current`, if they are equal, then add the index of current starting point to result, otherwise go check the next word. Since we setup several early stopping condition, if a word does not exist, we'll break the loop; if a word appears more times than it did in `words`, we'll break the loop as well. So the only case for a valid substring is when the number of words in `current` is equal to that of `count`


<img src="https://user-images.githubusercontent.com/25105806/121661746-61676c00-ca59-11eb-9a70-0c4182ed5391.gif" width="110%" height="110%">

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/findSubstring/findStringAnimation.ppsx) to download the animation to play for yourself.**

<br />

```python3
def findSubstringTwoMaps(self, s: str, words: List[str]) -> List[int]:
    result = list()
    # store the word and its frequency in a dict
    count = dict(Counter(words))
    wordLen = len(words[0])

    for strPtr in range(len(s)-wordLen*len(words) + 1):
        current = dict()
        window = s[strPtr:strPtr + wordLen]
        # i is used to keep track of how many words we've added to current dict
        # iterate over all word in words list
        for i in range(len(words)):
            if window in count:
                if window in current:
                    current[window] += 1
                    if current[window] > count[window]:
                        i-=1
                        break
                else:
                    current[window] = 1
            else:
                # the window word does not exist in words list
                # we can directly jump to the end of this word
                strPtr = strPtr + wordLen * (i+2)
                i-=1
                break
            # get next word
            window = s[strPtr + wordLen * (i+1): strPtr + wordLen * (i+2)]

        if i == len(words) - 1:
            result.append(strPtr)

    return result

```

Time complexity is reduced to O(mn):
![image](https://user-images.githubusercontent.com/25105806/121617512-fa769280-ca19-11eb-9bb6-2161e77d555d.png)






