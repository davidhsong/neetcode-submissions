class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 1

        if len(s) <= 1:
            return len(s)

        while r < len(s):
            if s[r] in s[l:r]:
                while s[r] in s[l:r]:
                    l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest