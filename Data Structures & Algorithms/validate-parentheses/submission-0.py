class Solution:
    def isValid(self, s: str) -> bool:
        opening = "[{("
        closing = ")}]"
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            if c in closing:
                stack.pop()
        return len(stack) == 0



        
