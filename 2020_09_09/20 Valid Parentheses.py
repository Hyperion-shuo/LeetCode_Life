class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {')': '(',
                 '}': '{',
                 ']': '['}

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return True if not stack else False