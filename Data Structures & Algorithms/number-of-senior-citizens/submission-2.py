class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for age in details:
            if int(age[11:13]) > 60:
                count += 1
        
        return count