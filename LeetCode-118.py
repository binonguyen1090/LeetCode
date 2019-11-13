# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        
        first_row = [1]
        result.append(first_row)
        
        for i in range(1,numRows):
            pre_row = result[i-1]
            cur_row = []
            cur_row.append(1)
            for j in range(1,i):
                sum = pre_row[j-1]+pre_row[j]
                cur_row.append(sum)
            cur_row.append(1)
            result.append(cur_row)
        return(result)