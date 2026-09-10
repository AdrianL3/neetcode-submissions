class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                #ASCII values
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

        #O(m * n)
        # m = number of wors, and n is average length of words