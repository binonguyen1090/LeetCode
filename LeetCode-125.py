# https://leetcode.com/problems/valid-palindrome/submissions/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        while left < right:
            while left < right and s[left] not in alpha:
                    left +=1
            while left < right and s[right] not in alpha: 
                    right -=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
                
        
        
        