class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = {}
        for i in word:
            count[i] = count.get(i,0)+1
        for let in count:
            count[let] -=1
            temp_freq = [val for val in count.values() if val>0]
            if len(set(temp_freq))==1:
                return True
            count[let] +=1
        return False