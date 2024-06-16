class UnionFind:
    def __init__(self):
        self.parents = {}

    def findParent(self, x):
        par = self.parents.get(x, x)
        if x != par: 
            self.parents[x] = self.findParent(par)    
            return self.parents[x]
        return x

    def union(self, x, y):
        self.parents[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))
