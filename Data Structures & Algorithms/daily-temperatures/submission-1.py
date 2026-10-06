class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                days = i - stack[-1][1]
                result[stack[-1][1]] = days
                stack.pop()
            stack.append((temperatures[i], i))

        
        return result