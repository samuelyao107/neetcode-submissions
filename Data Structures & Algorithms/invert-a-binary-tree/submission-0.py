# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def DFS(node):
            if node == None:
                return 
            DFS(node.left)
            temp = node.left
            node.left = node.right
            DFS(node.right) 
            node.right = temp 

        DFS(root)  
        return root    
        