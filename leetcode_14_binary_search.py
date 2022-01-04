class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        ans_index = 0
        left, right = 1, len(shortest)
        while left <= right:
            middle = (left + right) // 2
            if self.isCommonPrefix(shortest[:middle], strs):
                ans_index = middle
                left = middle + 1
            else:
                right = middle - 1
                
        return shortest[:ans_index]
            
        
    def isCommonPrefix(self, prefix: str, strs: List[str]) -> bool:
        for s in strs:
            if not s.startswith(prefix):
                return False
        return True
        