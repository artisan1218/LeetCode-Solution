# %%
from typing import List

class Solution:
    def minimumTotalDPbottomUp(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in reversed(triangle):
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i+1])
        return dp[0]

    def minimumTotalDPtopDown(self, triangle: List[List[int]]) -> int:
        curr_dp = [triangle[0][0]]
        for row in triangle[1:]:
            next_dp = [float('inf')] * len(row)
            for i in range(len(curr_dp)):
                next_dp[i] = min(curr_dp[i]+row[i], next_dp[i])
                next_dp[i+1] = min(curr_dp[i]+row[i+1], next_dp[i+1])
            curr_dp = next_dp
        return min(curr_dp)


if __name__ == '__main__':
    solver = Solution()

    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    result = solver.minimumTotalDPtopDown(triangle)
    print(result)
        


