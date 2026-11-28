class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for i in tokens:
            if i not in ops:
                stack.append(i)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if i == "+":
                    insert = num2 + num1
                elif i == "-":
                    insert = num2 - num1
                elif i == "*":
                    insert = num2 * num1
                else:
                    insert = num2 // num1
                stack.append(insert)
        return stack[0]
            
                