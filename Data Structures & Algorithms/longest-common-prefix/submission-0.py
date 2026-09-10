class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan each "col" of string until there is a mismatch
        for i in range(len(strs[0])):
            for word in strs:
                #index out of bounds or mismatch
                if i == len(word) or word[i] != strs[0][i]:
                    # only return the prefix up to the point we know matches
                    return strs[0][:i]
        # if the first word is a prefix for everything, we know it has to be the result
        # because it has no more characters to compare to
        return strs[0]