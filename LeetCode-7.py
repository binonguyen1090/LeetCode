# https://leetcode.com/problems/reverse-integer/

def reverse(self, x: int) -> int:
        if x > 0 :
            result = int(str(x)[::-1])
        if x <= 0 :
            result = -1*int(str(x*-1)[::-1])
            
        if result > 2**31-1 or result < -2**31 :
            result = 0
        return (result)