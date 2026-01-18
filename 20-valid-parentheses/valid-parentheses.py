class Solution:
    def isValid(self, s: str) -> bool:
        #opening  = ["(","[","{"]
        #obviously this has to be recursive
        #we are checking that for every opening there is a closing
        #and it is in the correct order
        #that means there will be some kind of check in the recursive call
        #I am assuming that all openers will exist then closers
        #this assumption is quickly debunked because there will exits
        #()[]
        #recursive call will be made on a condition?
        #if str is in opening
        #then we will call isValid again with the substring of everything after str
        #if it is a closer then we start comparing?
        #base case is empty substr?

        #stack attempt

        opening  = ["(","[","{"]
        closing  = [")","]","}"]
        pairs = {")":"(",
                 "]":"[",
                 "}":"{"}

        stack = deque()

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                openBracket = stack.pop()
                if openBracket != pairs[bracket]:
                    return False

        return not stack
                


        