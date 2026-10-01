class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

            max_freq = max(max_freq, count[s[i]])

            window_length = i - left + 1
            replacements = window_length - max_freq

            if replacements > k:
                count[s[left]] -= 1
                left += 1
        
            result = max(result, i - left + 1)

        return result
