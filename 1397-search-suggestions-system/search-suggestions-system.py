class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographically order of products
        ans = []
        startIdx, endIdx = 0, n - 1
        # for each letter in searchWord
        for i, c in enumerate(searchWord):
            # while the start idx and end idx dont collide
            # and i does not exceed the max idx or the ith letter is less than letter in saerchword
            while startIdx <= endIdx and (i >= len(products[startIdx]) or products[startIdx][i] < c):
                # then move the idx to right 
                startIdx += 1
            # and the same bot from the right side, till we fix the end idx
            while startIdx <= endIdx and (i >= len(products[endIdx]) or products[endIdx][i] > c):
                endIdx -= 1

            # if start idx is less than the end idx
            if startIdx <= endIdx:
                # take the range of minimum of either the end or the first 3
                ans.append(products[startIdx:min(startIdx+3, endIdx+1)])
            else:
                # else nothing
                ans.append([])
        return ans