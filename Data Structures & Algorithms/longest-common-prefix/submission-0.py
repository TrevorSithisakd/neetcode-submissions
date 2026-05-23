class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # save prefix first loop check all words see if breaks then start from new word
        pre = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(pre), len(strs[i])):
                if strs[i][j] != pre[j]:
                    break

                j += 1
            pre = pre[:j]
        return pre