#https://leetcode.com/problems/length-of-last-word/submissions/
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
        
#         local_count = 0
#         result = 0
#         for i in range(0,len(s)):
#             if s[i] == ' ':
#                 local_count = 0
#             else:
#                 local_count += 1
#                 result = local_count
#         return(result)
            
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s.endswith(' '):
            s = s[0:-1]
        arr = s.split(' ')
        return (len(arr[-1]))
            