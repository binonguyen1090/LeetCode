#https://leetcode.com/problems/plus-one/submissions/
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         total = 0
#         for i in digits:
#             total = total*10 + i
#         s = str(total+1)
#         result = list(s)
#         return(result)
            


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return([1,0])
            else:
                
                return self.plusOne(digits[:-1]) + [0]
        digits[-1] = digits[-1]+ 1
        return(digits)