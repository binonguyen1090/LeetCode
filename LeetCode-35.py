
# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == target:
                return(i)
            else:
                nums.append(target)
        
        
        nums.sort()
        for k in range (0,len(nums)):
            if nums[k] == target:
                return(k)


