# https://leetcode.com/problems/pascals-triangle-ii/submissions/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] + [0]*rowIndex
        for i in range(0,rowIndex):
            for j in range(i+1,0,-1):
                result[j] += result[j-1]
        return result
        