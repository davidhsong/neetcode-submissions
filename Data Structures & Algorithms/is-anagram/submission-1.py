class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check base-case
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
        # create hashmap for char count:
            # key = char
            # value = count
        #count = {}


