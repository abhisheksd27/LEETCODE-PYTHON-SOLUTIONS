class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat=0
        while(nums):
            if len(nums)==1:
                concat+=nums.pop()
            else:
                concat += int(str(nums.pop(0))+ str(nums.pop()))
        return concat        
        