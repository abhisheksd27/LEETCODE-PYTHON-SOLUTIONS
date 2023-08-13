class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=[]
        for i in range(len(s)):
            l=s.count(s[i])
            if l==1:
               arr.append(i)
               break
        if len(arr)==1:
            return arr[0]
        else:
            return -1
            
            