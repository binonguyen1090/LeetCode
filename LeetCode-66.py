#https://leetcode.com/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i in digits:
            total = total*10 + i
        s = str(total+1)
        result = list(s)
        return(result)
            