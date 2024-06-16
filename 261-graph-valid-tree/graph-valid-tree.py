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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree must follow two criteria
        # 1) No cycles
        # 2) Single Connected Componenent
        dsu = UnionFind()
        for x, y in edges: 
            if dsu.findParent(x) == dsu.findParent(y): 
                return False
            dsu.union(x, y)
        numComponents = len(set(dsu.findParent(x) for x in range(n)))
        return numComponents == 1