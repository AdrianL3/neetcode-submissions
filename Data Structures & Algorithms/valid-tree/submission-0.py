class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #obvious case, if there are more than n -1 edges
        if len(edges) > (n -1):
            return False

        adj = [[] for i in range(n)]

        for u,v in edges:
            #since its undirected, add edges to both nodes
            adj[u].append(v)
            adj[v].append(u)
        #initialze a visit array to keep track whether a node has been seen
        visit = set()

        #recurse with node and prev so we can avoid false positives
        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                #if the nei is prev(where we came from) ignore it
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    False
            return True

        #dfs return true, and every node is connected
        return dfs(0, -1) and n == len(visit)