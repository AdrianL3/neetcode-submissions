class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        #the stack is monotonicly decreasing and will always have values less than top added

        for i, t in enumerate(temperatures):
            #while there is a value that is greater, remove from the stack and update the result
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res