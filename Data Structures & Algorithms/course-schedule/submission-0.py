class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build the adjacency list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #visit set to see all the current courses to check for loops
        visitSet = set()
        def dfs(crs):
            #base case loop
            if crs in visitSet:
                return False
            #base case if preReq is empty, then class can be compelted
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            #recurse through every neighbor in the current course to check
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            #if we know the course can be visited, we can make it an empty list to show that it can be taken
            preMap[crs] = []
            return True

        #have to call the dfs on every single course to check
        #this is because not all classes are gaurenteed to be connected to each other
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True