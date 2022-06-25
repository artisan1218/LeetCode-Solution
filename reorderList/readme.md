# Restore IP Addresses problem
![image](https://user-images.githubusercontent.com/25105806/135189873-648db0b7-642f-4061-8b71-449c4acfd4bb.png)

Leetcode link: https://leetcode.com/problems/restore-ip-addresses/

<br />

### Approach 1: Backtracking, backtrack(), restoreIpAddresses()
The idea is to exhaust all possible combinations at each digit and use pruning as early stopping condition to avoid invalid computations. For exmaple when we have '1', we can each keep it as a valid digit or appending another digit to it, until the digit is no longer valid.

```python3
def restoreIpAddresses(self, s: str) -> List[str]:
    result = []
    self.backtrack(s, result, [], 0)
    return ['.'.join(address) for address in result]

def backtrack(self, s, result, current, start):
    if start<=len(s) and len(current)<=4: # pruning
        if len(current)==4 and sum([len(digit) for digit in current])==len(s):
            result.append(current.copy())
        else:
            for i in range(1, 4): # only get up to next 3 letters
                digit = s[start:start+i]
                if len(digit)==1 or (len(digit)>1 and digit[0]!='0' and int(digit)<=255):
                    current.append(digit)
                    self.backtrack(s, result, current, start+i)
                    current.pop()
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/135190094-15422c5e-ad2e-49e7-9a60-931f89ba8409.png)

