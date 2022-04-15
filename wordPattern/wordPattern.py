#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            wordList = s.split(' ')
            if len(wordList) == len(pattern):
                word2p = dict()
                p2word = dict()
                for word, p in zip(wordList, pattern):
                    if word not in word2p:
                        word2p[word] = p
                    elif word2p[word] != p:
                            return False

                    if p not in p2word:
                        p2word[p] = word
                    elif p2word[p] != word:
                            return False
                return True
            else:
                return False


if __name__ == '__main__':
    solver = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(solver.wordPattern(pattern, s))

