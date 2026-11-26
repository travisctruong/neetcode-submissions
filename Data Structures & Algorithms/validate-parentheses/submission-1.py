class Solution:
    def isValid(self, s: str) -> bool:
        opening = "[{("
        closing = ")}]"
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            if c in closing:
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0



        
