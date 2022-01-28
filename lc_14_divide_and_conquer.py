class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def divide(arr:List[str], left: int, right: int) -> str:
            if left >= right:
                return arr[left]
            mid = (left + right) // 2
            left_common = divide(arr, left, mid)
            right_common = divide(arr, mid + 1, right)
            
            return conquer(left_common, right_common)
        
        def conquer(a: str, b: str) -> str:
            result = ""
            if len(a) > len(b):
                a, b = b, a
            for i, ch in enumerate(a):
                if ch != b[i]: 
                    break
                result += ch
            return result
        
        return divide(strs, 0, len(strs) - 1)
            