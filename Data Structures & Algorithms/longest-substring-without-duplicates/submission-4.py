class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            previous_index = last_seen.get(char, -1)

            if previous_index >= left:
                left = previous_index + 1

            last_seen[char] = right

            current_length = right - left + 1
            if current_length > longest:
                longest = current_length

        return longest