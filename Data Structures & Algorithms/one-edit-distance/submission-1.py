class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """"
        base cases
        if abs diff of lens > 1 or s == t
        then we return false

        helper function (handles when len(s) == len(t))

        helper function (handles when abs(len(s) - len(t)) == 1)
        """""
        lenS = len(s)
        lenT = len(t)
        if abs(lenS - lenT) > 1 or s == t:
            return False

        def sameLength(s, t):
            operation = True

            for i in range(lenS):
                if operation and s[i] != t[i]:
                    operation = False
                elif not operation and s[i] != t[i]:
                    return False
                
            return True

        def diffLength(short, longer):
            operation = True

            for i in range(len(short)):
                #consider if not the same charcter
                if operation and short[i] != longer[i]:
                    operation = False
                    if short[i] != longer[i + 1]:
                        return False
                elif not operation and short[i] != longer[i +1]:
                    return False
            
            return True
        
        if lenS == lenT:
            return sameLength(s,t)
        else:
            if lenS < lenT:
                return diffLength(s, t)
            else:
                return diffLength(t, s)


