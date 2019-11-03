#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if (len(strs) == 0):
           return (result)

        for i in range (0, len(strs[0])):
          chara = strs[0][i]
          for k in range (1,len(strs)):
          
            if (i == len(strs[k]) or strs[k][i] != chara):
                return(result)
          result += chara
        return (result)

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         result = ""
#         if len(strs) == 'null' or len(strs) == 0:
#             return(result)
#         elif len(strs) == 1:
#             return strs[0]
#         else:
#             l = len(strs[0])
#             shorted = ""
#             for i in range(0,len(strs)):
#               if len(strs[i]) <= l:
#                 l = len(strs[i])
#                 shorted = strs[i]

            
#             for j in range(0,len(shorted)):

#               if check(shorted[j],strs,j):
#                 result+=(shorted[j])
#               else:
#                 return (result)

#             print(result)
#             return(result)

    
# def check(s,a,i):
#   for word in a:
#     if s != word[i]:
#       return False
#   return True