# Restore IP Addresses problem
![image](https://user-images.githubusercontent.com/25105806/135189873-648db0b7-642f-4061-8b71-449c4acfd4bb.png)


### Approach 1: Backtracking, backtrack(), restoreIpAddresses()
The idea is to exhaust all possible combinations at each digit and use pruning as early stopping condition to avoid invalid computations. For exmaple when we have '1', we can each keep it as a valid digit or appending another digit to it, until the digit is no longer valid.

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135190094-15422c5e-ad2e-49e7-9a60-931f89ba8409.png)

