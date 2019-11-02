# https://leetcode.com/problems/palindrome-number/


def isPalindrome(self, x: int) -> bool:
        cop = x
        rev = 0
        while cop > 0:
            a = cop %10
            rev = rev*10 + a
            cop = int(cop/10)

        if rev == x:
            return True
        else:
            return False

