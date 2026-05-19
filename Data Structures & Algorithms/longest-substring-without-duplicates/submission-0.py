class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force 
        # loop through each store char as you go 
        # how to check if in the rest of the string 
        # stop for if same character exists in the same string already
        res = 0
        for i in range(len(s)):
            char = set()
            for j in range(i, len(s)):
                # add to set if not same char or in set already 
                if s[j] in char:
                    break
                char.add(s[j])

            res = max(res, len(char))

        return res