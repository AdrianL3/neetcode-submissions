class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    num = first + second
                elif token == "-":
                    num = first - second
                elif token == "*":
                    num = first * second
                else:
                    num = int(first / second)
                stack.append(num)
            else:
                stack.append(int(token))

        return stack[-1]