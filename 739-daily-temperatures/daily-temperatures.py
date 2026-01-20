class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #my instant and initial thought was to use two pointers and whenever I found a solution I would advance left by 1 and put right = left but I am not sure how that would work against a large temperatures list
        res = [0] * len(temperatures)
        stack = [] #this will store a tuple. temp and index

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackTemperature = stack.pop()
                res[stackIndex]= i - stackIndex
            stack.append([i,t])
        return res