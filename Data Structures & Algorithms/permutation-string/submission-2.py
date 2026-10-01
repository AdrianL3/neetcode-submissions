class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        first = {}
        second = {}

        s1Len = len(s1)
        s2Len = len(s2)

        for ch in s1:
            first[ch] = first.get(ch, 0) + 1

        for i in range(len(s1)):
            second[s2[i]] = second.get(s2[i], 0) + 1

        if first == second:
                return True

        for j in range(s1Len, s2Len):
            # move left pointer
            second[s2[j - s1Len]] -= 1
            if second[s2[j - s1Len]] == 0:
                del second[s2[j - s1Len]]

            if s2[j] in second:
                second[s2[j]] += 1
            else:
                second[s2[j]] = 1
                
            if first == second:
                return True

        return False