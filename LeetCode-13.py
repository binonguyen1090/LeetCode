#https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        a = {"I"  : 1,
                "V"     :       5,
                "X"       :      10,
                "L"      :      50,
                "C"        :     100,
                "D"       :     500,
                "M"        :    1000}


        l = len(s)
        last = a[s[-1]]
        total = last



        for i in range(l-1,0,-1):

          numR = a[s[i]]
          numL = a[s[i-1]]
          if numR <= numL:

            total += numL
          else:

            total -= numL
        print(total)
        return(total)