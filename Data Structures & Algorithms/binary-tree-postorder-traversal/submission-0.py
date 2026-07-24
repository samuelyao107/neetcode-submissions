# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []

        def DFS(node):
            if node == None: 
                return
             
            DFS(node.left)
            if node.left != None:
                visited.append(node.left.val)
            DFS(node.right)
            if node.right != None:
                visited.append(node.right.val)
        DFS(root)
        if root != None:
            visited.append(root.val)
        return visited

                
        