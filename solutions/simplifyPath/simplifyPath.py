#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = list()
        pathList = path.split('/')
        for directory in pathList:
            # skip '' and .
            if directory!='' and directory!='.':
                if directory == '..':
                    # go back to previous dir
                    if len(result)==1:
                        result[0] = '/'
                    elif len(result)>1:
                        result.pop()
                    else:
                        # root dir
                        result.append('/')
                else:
                    if len(result) > 0 and result[-1] == '/':
                        result.append('{}'.format(directory))
                    else:
                        result.append('/{}'.format(directory))
        if len(result)==0:
            return '/'
        else:
            return ''.join(result)
        
if __name__ == "__main__":
    solver = Solution()
    path = "/"
    print(solver.simplifyPath(path))


# In[ ]:




