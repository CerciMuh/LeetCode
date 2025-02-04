from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for x in s: 
            if x in bracket_map.values():  
                stack.append(x)
            elif x in bracket_map:  
                if not stack or stack.pop() != bracket_map[x]:
                    return False

        return not stack 
