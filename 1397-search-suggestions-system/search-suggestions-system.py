class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        for i in range(len(searchWord)):
            matches = []
            counter = 0
            for p in products:

                if p[:i+1] == searchWord[:i+1]:
                    counter += 1
                    matches.append(p)
                    if counter == 3:
                        break
            result.append(matches)
        
        return result
