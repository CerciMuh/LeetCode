class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': lambda a,b: a + b,
                    '*': lambda a,b: a * b,
                    '-': lambda a,b: a - b,
                    '/': lambda a,b: int( a / b )}
        result = 0 
        for  token in tokens: 
            if token in operators :
                a = stack.pop()
                b=stack.pop()
                stack.append(operators[token](b,a))
            else: 
                stack.append(int(token))

        return stack[0]