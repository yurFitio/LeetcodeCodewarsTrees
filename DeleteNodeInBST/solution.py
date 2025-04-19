# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            min_larger_val = cur.val
            root.val = min_larger_val
            root.right = self.deleteNode(root.right, min_larger_val)

        return root

# # [5,3,6,2,4,null,7]
# a = Solution()
# b = a.deleteNode(TreeNode(3, TreeNode(1, TreeNode(0.5), TreeNode(2)), TreeNode(4)), 1)
