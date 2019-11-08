
#https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(0, n-1):
            s = generate(s)
        print(s)
        return(s)
            
            
def generate(s):
    result = []
    i = 0
    
    while i < len(s):
        count = 1
        while i < int(len(s)-1) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return(''.join(result))
