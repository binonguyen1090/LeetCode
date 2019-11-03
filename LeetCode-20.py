# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        arr = []
        for chara in s:
            if chara in pairs:
                arr.append(pairs[chara])
            else:
                if len(arr) == 0 or chara != arr.pop():
                    return False
        
        return len(arr) == 0