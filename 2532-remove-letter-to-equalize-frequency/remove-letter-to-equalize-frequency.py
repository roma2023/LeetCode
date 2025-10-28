class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        for ch in list(cnt.keys()):
            cnt[ch] -= 1
            if cnt[ch] == 0:
                del cnt[ch]
            # collect positive counts and see if they are all equal
            freqs = set(cnt.values())
            if len(freqs) == 1:
                return True
            # restore
            cnt[ch] = cnt.get(ch, 0) + 1
        return False
            


        
        