# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2

# Output: 1

# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.smallest = []

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        queue = []
        if root:
            queue.append(root)

        while queue:
            root = queue.pop(0)
            self.smallest.append(root.val)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        sl = sorted(self.smallest)
        return sl[k - 1]



