class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backTrack(numOpen,numClosed):
            if numOpen == numClosed == n:
                result.append("".join(stack))
            if numOpen<n:
                stack.append("(")
                backTrack(numOpen+1,numClosed)
                stack.pop()
            if numClosed<numOpen:
                stack.append(")")
                backTrack(numOpen,numClosed+1)
                stack.pop()
            

        backTrack(0,0)              
        return result    