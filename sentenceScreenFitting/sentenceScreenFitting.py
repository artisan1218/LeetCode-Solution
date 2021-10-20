#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List
class Solution:
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
    
if __name__ == '__main__':
    solver = Solution()
    sentence = ["hello","world"]
    rows = 2
    cols = 8
    print(solver.wordsTyping(sentence, rows, cols))


# In[ ]:




