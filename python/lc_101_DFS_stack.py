class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        stack = [[root.left, root.right]]
        
        while stack:
            left, right = stack.pop()
            if left is None and right is None: continue
            elif left is None or right is None: return False
            elif left.val != right.val: return False
            
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        return True