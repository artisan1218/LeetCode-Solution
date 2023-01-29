# Letter Combinations of a Phone Number problem
* Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.\
![image](https://user-images.githubusercontent.com/25105806/119457090-27276c00-bcf0-11eb-8df6-5298d86de581.png)

Leetcode link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

<br/>

### Approach 1: Combinations, letterCombinations()
The idea is taken from BFS, the number read in in order can be considered as levels of a tree. For example, when reading `23`, we first append `['a', 'b', 'c']` to the list, then we read number `3`, then we concatenate `'d', 'e', 'f'` to **each of the `['a', 'b', 'c']`**. So it becomes `['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']`.\
Keep this process going until we reach the end of input `digits`.\
<img src="https://user-images.githubusercontent.com/25105806/119458456-9f426180-bcf1-11eb-9c63-051171a1fe84.png" width="35%" height="35%">


```python
def letterCombinations(digits: str) -> List[str]:
    if len(digits)==0:
        return []
    else:
        mapping = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        prev_list = ['']
        for d in digits:
            letters = mapping[d]
            result_list = [prefix+letter for prefix in prev_list for letter in letters]
            prev_list = result_list
        return result_list
```

Time complexity is O(4^n) because each digit can be presented at most by 4 letters. On each iteration we go over all 4 of them. And we do this n (the number of digits) time.\
![image](https://user-images.githubusercontent.com/25105806/119459158-4cb57500-bcf2-11eb-95fb-9358162d7662.png)



