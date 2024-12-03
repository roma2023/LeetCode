class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False


class MagicDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.trie
            for ch in word:
                cur = cur.children[ch]
            cur.is_end = True
        

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        def dfs(root: TrieNode, cnt: int, i: int) -> bool:
            if cnt > 1 or i == n: return cnt == 1 and root.is_end
            return any([dfs(root.children[c], cnt + int(c != searchWord[i]), i + 1) for c in root.children])
        
        return dfs(self.trie, 0, 0)
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

