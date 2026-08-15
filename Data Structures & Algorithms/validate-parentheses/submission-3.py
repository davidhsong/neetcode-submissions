class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                if not stack or stack[-1] != pairs.get(c):
                    return False
                stack.pop()
            
        if stack:
            return False
        return True