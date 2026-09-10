class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ""

        for char in s:
            if char.isalnum():
                chars += char.lower()
        

        return chars == chars[::-1]