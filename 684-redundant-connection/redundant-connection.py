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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind()
        for x, y in edges: 
            if dsu.findParent(x) == dsu.findParent(y): 
                return [x,y]
            dsu.union(x, y)