class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        word1 = {}

        for char in s1:
            if char not in word1:
                word1[char] = 1
            else:
                word1[char] += 1
        
        #inititalize first window
        word2 = {}

        for i in range(len(s1)):
            if s2[i] not in word2:
                word2[s2[i]] = 1
            else:
                word2[s2[i]] += 1

        # Check the first window
        if word1 == word2:
            return True

        window_size = len(s1)

        #sliding window
        for i in range(len(s1), len(s2)):
            
            # char leaving the window
            left_char = s2[i - window_size]
            word2[left_char] -= 1
            if word2[left_char] == 0:
                word2.pop(left_char)

            if s2[i] not in word2:
                word2[s2[i]] = 1
            else:
                word2[s2[i]] += 1

            #check if the dictionary is equal
            if word1 == word2:
                return True

        return False