class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            suggestions = []

            for p in products:
                if p.startswith(prefix):
                    suggestions.append(p)
                if len(suggestions) == 3:
                    break
                
            result.append(suggestions)

        return result