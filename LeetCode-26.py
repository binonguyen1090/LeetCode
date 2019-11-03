# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = 1
        
#         while index < len(nums):
#             if nums[index] == nums[index-1]:
#                 nums.remove(nums[index])
#             else:
#                 index += 1
#         return(len(nums))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        
        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index +=1
        return(index)
