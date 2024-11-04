class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LCS = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]: 
                    LCS[i][j] = 1 + LCS[i+1][j+1]
                else: 
                    LCS[i][j] = max(LCS[i+1][j], LCS[i][j+1])

        return LCS[0][0]