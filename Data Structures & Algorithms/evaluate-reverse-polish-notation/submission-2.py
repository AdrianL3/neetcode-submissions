import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = tokens[0]
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for num in tokens:
            if num in ops:
                second = stack.pop()
                first = stack.pop()

                curr = ops[num](first, second)
                stack.append(curr)
            else:
                stack.append(int(num))
        return stack[-1]