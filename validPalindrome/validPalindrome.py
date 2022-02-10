# %%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s)-1
        while front < back:
            if not s[front].isalnum():
                front += 1
                continue # go directly to the next iteration without checking equality
            if not s[back].isalnum():
                back -= 1
                continue # go directly to the next iteration without checking equality
            
            if s[front].lower() == s[back].lower():
                front += 1
                back -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    solver = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solver.isPalindrome(s))

# %%



