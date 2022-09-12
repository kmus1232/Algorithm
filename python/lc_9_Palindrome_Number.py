class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        length = len(str_x)
        for i in range(len(str_x) // 1):
            if str_x[length - 1 - i] != str_x[i]:
                return False
        return True

