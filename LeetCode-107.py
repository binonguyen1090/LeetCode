# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return([])
        result = []
        level = [root]
        
        while level:
            temp = []
            vals = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                vals.append(node.val)
                
            level = temp
            result.append(vals)
        return result[::-1]