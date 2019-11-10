# https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        
        for i in range (m+n+1,-1,-1):
            if n == -1:
                nums1[i] = nums1[m]
                m-=1
            elif m == -1:
                nums1[i] = nums2[n]
                n-=1
            elif nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else: 
                nums1[i] = nums2[n]
                n -= 1
        return(nums1)