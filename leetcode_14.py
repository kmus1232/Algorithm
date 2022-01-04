class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min([len(word) for word in strs])
        ans = ""
        for i in range(shortest):
            cur = strs[0][i]
            break_flag = False
            for word in strs:
                if cur != word[i]:
                    break_flag = True
                    break
            if break_flag == True:
                break
            ans += cur
        return ans
         
