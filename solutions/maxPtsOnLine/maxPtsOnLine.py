# %%
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        else:
            # calculate slopes between all pairs in the points, if two pairs have the same slope and start with a same point, they are on the same line
            curMax = 0
            for src in points:
                # slopeDict:
                # key: slope between src and dst
                # value: number of dst points that fall on the line that starts with src
                # so slopeDict contains the number of points on a line starts with different src point
                slopeDict = dict()
                for dst in points:
                    if src!=dst:
                        # calculate slope
                        delta_x = dst[0] - src[0]
                        delta_y = dst[1] - src[1]
                        slope = float('inf') if delta_x == 0 else delta_y / delta_x

                        if slope in slopeDict:
                            slopeDict[slope]+=1
                        else:
                            slopeDict[slope]=2
                curMax = max(curMax, max(slopeDict.values()))

            return curMax
        

if __name__ == "__main__":
    solver = Solution()
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    result = solver.maxPoints(points)
    print(result)

# %%



