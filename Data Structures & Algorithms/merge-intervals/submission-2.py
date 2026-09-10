class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x: x[0])

        result = []
        start = sorted_list[0][0]
        end = sorted_list[0][1]

        for interval in sorted_list:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                result.append([start, end])
                start = interval[0]
                end = interval[1]

        result.append([start, end])
        return result