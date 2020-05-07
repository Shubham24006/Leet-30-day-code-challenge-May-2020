# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins
#
#
# Example 1:
# Input: root = [1, 2, 3, 4], x = 4, y = 3
# Output: false
# Example
# 2:
#
# Input: root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4
# Output: true
# Example
# 3:
#
# Input: root = [1, 2, 3, null, 4], x = 2, y = 3
# Output: false
#
# Note:
# 1) The number of nodes in the tree will be between 2 and 100.
# 2) Each node has a unique integer value from 1 to 100.


# Solution

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        l1 = []
        l2 = []

        self.iterate(None, root, 0, x, l1)
        self.iterate(None, root, 0, y, l2)
        if l1[0][0] != l2[0][0] and l1[0][1] == l2[0][1]:
            return True

        return False

    def iterate(self, parent, root, depth, val, ls):
        if not root:
            return None

        if root.val == val:
            ls.append((parent, depth))

        self.iterate(root, root.left, depth + 1, val, ls)
        self.iterate(root, root.right, depth + 1, val, ls)

