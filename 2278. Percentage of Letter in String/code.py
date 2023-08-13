class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        start_index=0
        l=len(s)
        for i in range(l):
            j = s.find(letter,start_index)
            if(j!=-1):
                start_index = j+1
                count+=1
        per = math.floor((count/l)*100)
        return per

