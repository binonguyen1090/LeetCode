#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = result = nums[0]
        for i in range ( 1,len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            if max_current > result:
                result = max_current
        return(result)
        