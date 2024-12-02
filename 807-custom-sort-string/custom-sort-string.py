class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1

        res = []
        for char in order:
            if char in hashMap:
                freq = hashMap[char]
                res.append(char * freq)
                del hashMap[char]
        print(res)

        for char, freq in hashMap.items():
            res.append(char * freq)
        print(res)
        return "".join(res)

