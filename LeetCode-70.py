#https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for i in range(2,n+1):
            result = arr[i-1] + arr[i-2]
            arr.append(result)
        return arr[-1]