class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyStore:
            currList = self.keyStore[key]
        else:
            return ""

        l, r = 0, len(currList) - 1
        res = ""
        # 1 3 5
        while l <= r:
            m = (l + r) // 2
            
            if currList[m][0] <= timestamp:
                res = currList[m][1]
                l = m + 1
            else:
                r = m - 1

        return res


