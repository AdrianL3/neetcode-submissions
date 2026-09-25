class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                resultSum = record[-1] + record[-2]
                record.append(resultSum)
            elif op == "D":
                resultSum = record[-1] * 2
                record.append(resultSum)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        
        result = 0

        for num in record:
            result += num

        return result