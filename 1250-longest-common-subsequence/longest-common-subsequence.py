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
    
# TC = O(nm), SC = O(nm)



# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
#         L = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]

#         def LCS (i, j): 
#             if i < 0 or j < 0 or i > len(text1) - 1 or j > len(text2) - 1: 
#                 return 0
            
#             if text1[i] == text2[j]: 
#                 if L[j][i]: 
#                     return L[j][i] 
#                 ret = 1 + LCS(i + 1, j + 1)
#                 L[j][i] = ret
#                 return ret
#             else: 
#                 if L[j][i]: 
#                     return L[j][i] 
#                 ret = max(LCS(i + 1, j), LCS(i, j + 1))
#                 L[j][i] = ret
#                 return ret
        
#         return LCS(0, 0)