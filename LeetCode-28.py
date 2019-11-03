
#https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or needle == haystack:
            return (0)
        for i in range(0,len(haystack)-len(needle)+1): 
            if haystack[i:i+len(needle)] == needle:
                return(i)
            
        return(-1)
        