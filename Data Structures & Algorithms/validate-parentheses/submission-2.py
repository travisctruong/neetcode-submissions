class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in dic.values():
                stack.append(c)
            if c in dic:
                if dic[c] in stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0



        
