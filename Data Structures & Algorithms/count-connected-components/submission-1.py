class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build adjacency list
        #n is how many different nodes there are, so one for each
        adj = [[] for _ in range(n)]
        for u,v in edges:
            #since its undirected, add edges to both nodes
            adj[u].append(v)
            adj[v].append(u)
        #initialze a visit array to keep track whether a node has been seen
        visit = [False] * n

        def dfs(node):
            for neig in adj[node]:
                #if the neighbor hasn't been seen yet. recurse on it
                if not visit[neig]:
                    visit[neig] = True
                    dfs(neig)

        res = 0
        #for the first node not seen, it will visit all its neighbors and
        # make a new connected componenet
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1

        return res