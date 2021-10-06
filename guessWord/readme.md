# Guess the Word Problem

![image](https://user-images.githubusercontent.com/25105806/136274216-6459ea8e-2d61-48ba-b28c-e09d970950a3.png)


<br />

### Approach 1: findSecretWord()
The idea is to randomly pick a word from `wordlist` and take a guess, if there are `x` matched chars, we then filter the `wordlist` to keep only words that has `x` matched chars with the randomly picked word. This way we can maximize the probability of next word will be `secret`.

credits to: https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            guess = random.choice(wordlist) # randomly get a word from wordlist
            x = master.guess(guess)
            # select only from word with at least x same char as guess to maximize prob
            wordlist = [w for w in wordlist if self.match(guess, w) == x]
        
        
    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))  
```

Time complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/136274625-090e323e-72c1-4d9e-b578-f577d2f95562.png)

