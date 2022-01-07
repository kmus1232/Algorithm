# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None: return True
        elif (root.left == None) ^ (root.right == None): return False
        
        l_q, r_q = deque(), deque()
        l_q.append(root.left)
        r_q.append(root.right)
        
        while l_q and r_q:
            left = l_q.popleft()
            right = r_q.popleft()
            if left.val != right.val: return False
            if (left.left == None) ^ (right.right == None): return False
            if (left.right == None) ^ (right.left == None): return False
            if left.left:
                l_q.append(left.left)
                r_q.append(right.right)
            if left.right:
                l_q.append(left.right)
                r_q.append(right.left)
        return True
