# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return check(root.left, root.right)
def check(left,right):
    if left is None or right is None:
        return left == right
    
    if left.val != right.val:
        return False
    
    return check(left.left,right.right) and check(left.right, right.left)