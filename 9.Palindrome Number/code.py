class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        pal=0
        number=x
        while(x>0):
            rem=x%10
            x=x//10
            pal=pal*10+rem
        return number==pal