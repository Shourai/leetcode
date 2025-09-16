from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    arr = []
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.LevelOrder(root)

    def LevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.CurrentLevel(root, i)
        return(self.arr)

    def CurrentLevel(self, root , level):
        if root is None:
            return
        if level == 1:
            self.arr.append(root.val)
        elif level > 1 :
            self.CurrentLevel(root.right , level-1)
            self.CurrentLevel(root.left , level-1)

    def height(self, node):
        if node is None:
            return 0
        else :
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().LevelOrder(root))
