class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        scale = 1

        for i in range(len(digits) - 1, -1, -1):
            result += digits[i] * scale
            scale *= 10

        result += 1
        res = []

        for char in str(result):
            res.append(int(char))

        return res