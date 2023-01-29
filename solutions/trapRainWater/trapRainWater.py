
from typing import List

class Solution:
    
    # TLE
    def trapCalculateFromTallestHeight(self, height: List[int]) -> int:
        result = 0
        
        # list of pair of (height of a bar, index of a bar)
        pairList = list()
        for idx, bar in enumerate(height):
            pairList.append((bar, idx))
        # sorted list by height of the bar in descending order
        pairList = sorted(pairList, key=lambda pair:(-pair[0], pair[1]))
        pairList = [pair for pair in pairList if pair[0]>0]
        
        coveredRangeL = float('inf')
        coveredRangeR = float('-inf')
        
        left, right = 0, 0
        while left < len(pairList)-1:
            right = left + 1
            while right < len(pairList):
                currRangeL = min(pairList[left][1], pairList[right][1])
                currRangeR = max(pairList[left][1], pairList[right][1])
                if currRangeL<=coveredRangeL and currRangeR<=coveredRangeL or currRangeL>=coveredRangeR and currRangeR>=coveredRangeR:
                    
                    currBasinLeftIdx = min(pairList[left][1], pairList[right][1])
                    currBasinRightIdx = max(pairList[left][1], pairList[right][1])
                    currBasinLeftBar = height[currBasinLeftIdx]
                    currBasinRightBar = height[currBasinRightIdx]
                    
                    # calculate the volume of the current basin bounded by left and right
                    currBasinSide = min(currBasinLeftBar, currBasinRightBar)
                    currBasinBottom = currBasinRightIdx - currBasinLeftIdx - 1
                    currBasinVolume = currBasinSide * currBasinBottom

                    # remove the volume of the blocks in this basin
                    for block in height[currBasinLeftIdx+1:currBasinRightIdx]:
                        currBasinVolume -= block

                    result+=currBasinVolume

                    # update left and right boundary of the seen basin
                    coveredRangeL = min(currBasinLeftIdx, coveredRangeL)
                    coveredRangeR = max(currBasinRightIdx, coveredRangeR)
                    
                    # we've checked all intervals
                    if coveredRangeL == 0 and coveredRangeR == len(pairList)-1:
                        break
                right+=1
            left+=1
            
        return result
    
    def trapCalculateFromTallestHeightRecursion(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        return self.calculateInterval(height, left, right)
    
    def calculateInterval(self, height: List[int], left: int, right: int) -> int:
        
        # only calculate the volume in this interval
        interval = height[left:right+1]
        
        # list of pair of (height of a bar, index of a bar)
        pairList = list()
        for idx, bar in enumerate(interval):
            pairList.append((bar, left + idx))
        # sorted list by height of the bar in descending order
        pairList = sorted(pairList, key=lambda pair:(-pair[0], pair[1]))
        # remove all bar with height 0 because they will not be able to trap any water
        pairList = [pair for pair in pairList if pair[0]>0]
        
        result = 0
        if len(pairList)>1:
            # take the tallest two bar and calculate the volume in this basin bounded by these two bars
            bar1Height = pairList[0][0]
            bar2Height = pairList[1][0]
            leftBarIdx = min(pairList[0][1], pairList[1][1])
            rightBarIdx = max(pairList[0][1], pairList[1][1])
            volume = min(bar1Height, bar2Height) * (rightBarIdx-leftBarIdx-1)
            # remove any blocks within this basin that cannot hold water
            for block in height[leftBarIdx+1:rightBarIdx]:
                volume -= block
            result += volume
        else:
            return 0
        
        # the tallest two bars are the outer-most two bar that covers all volume in this interval
        # there is no need to calculate anymore, just return the current volume
        if leftBarIdx==left and rightBarIdx==right:
            return result
        else:
            result += self.calculateInterval(height, left, leftBarIdx)
            result += self.calculateInterval(height, rightBarIdx, right)
            return result
        
    def trapDP(self, height: List[int]) -> int:
        
        # scan from left to right, store the volume of water than can be stored with left boundary
        leftMax = list()
        currMax = 0
        for bar in height:
            currMax = max(bar, currMax)
            leftMax.append(currMax)

        # scan from right to left, store the volume of water than can be stored with right boundary 
        rightMax = list()
        currMax = 0
        for bar in reversed(height):
            currMax = max(bar, currMax)
            rightMax.append(currMax)
        rightMax.reverse()
            
        # the actual volume of water will be the minimum of two volumes minus the volume of blocks
        result = 0
        for i in range(len(height)):
            result += min(leftMax[i], rightMax[i]) - height[i]
        
        return result
    
if __name__ == "__main__":
    solver = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solver.trapDP(height))






