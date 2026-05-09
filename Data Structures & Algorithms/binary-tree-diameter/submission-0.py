# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def getHeight(node):
            if node== None:
                return 0
            
            lefth= getHeight(node.left)
            righth= getHeight(node.right)

            diametertn= lefth+righth
            self.diameter= max(self.diameter, diametertn)

            return 1 + max(lefth, righth)

        getHeight(root)
        return self.diameter

        