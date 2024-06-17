class Solution:
    # TC = O(n)
    # SC = O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window method with hashtable

        chars = set(s)
        hs = {i: 0 for i in chars} # value: key for key,value in dic.items()
        
        focus = s[0] # the focus char
        total = 0 # total number of chars in the window
        res = 0
        p = 0 # points to the head of the window

        for i in range(len(s)):
            hs[s[i]] += 1
            total += 1

            while total - hs[focus] > k:
                hs[focus] -= 1
                total -= 1
                p += 1
                focus = s[p]

            res = max(res, total)
        
        return max(res, min(len(s),max(hs.values()) + k) )
            


                    
    
                  
            
                 
                
        