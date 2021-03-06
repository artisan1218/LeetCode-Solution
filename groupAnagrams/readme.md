# Group Anagrams problem
* Given an array of strings `strs`, group the anagrams together. 
* You can return the answer in any order.
* An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
* `eat` and `ate` are anagrams because they are consist of exact same letters.

Leetcode link: https://leetcode.com/problems/group-anagrams/

<br />

### Approach 1: Sort, groupAnagramsSort()

Since anagrams are the words that contain exactly same characters, we can sort each word so that each anagram can be represented by same word. Therefore hash them into a dict to group them.


```python3
def groupAnagramsSort(self, strs: List[str]) -> List[List[str]]:
    result = {}
    for word in strs:
        # all anagrams will have same value of sortedWord, so we can put them in a dict
        sortedWord = tuple(sorted(word))
        result[sortedWord] = result.get(sortedWord, []) + [word]

    return list(result.values())
```


Time complexity is therefore O(n\*klogk) where n is the number of words in the `strs` and k is the length of the longest word in `strs`. O(klogk) is to sort each word:

![image](https://user-images.githubusercontent.com/25105806/125178757-848e5400-e19c-11eb-8ec3-bc0ab3677b82.png)

<br />

### Approach 2: Count, groupAnagramsCount()

Instead of sorting to make all anagrams to be the same word, we can also count the occurence of each letter in each word.\
For example `eat` can be represented as `a:1, e:1, t:1` and `ate` can also be represented as `a:1, e:1, t:1`. This way, we group each anagram by their count.\
Note that I use a list of 26 indices to represent the count list to avoid sorting.

```python3
def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
    result = {}
    for word in strs:
        count = [0] * 26
        # count the occurence of each letter instead of sorting
        for char in word:
            count[ord(char)-ord('a')] += 1
        # convert type list to tuple to hash in dict
        result[tuple(count)] = result.get(tuple(count), []) + [word]

    return list(result.values())   
```


Time complexity is O(n\*k\*m), where n is the number of words in `strs`, k is the length of initial count list, m is the length of longest word because we need to iterate over each word to get the count.\
![image](https://user-images.githubusercontent.com/25105806/125178844-4e9d9f80-e19d-11eb-9788-e856374d8195.png)
