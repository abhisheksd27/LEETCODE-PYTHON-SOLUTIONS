class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        l=len(nums)
        for i in range(l):
            p=0
            for j in range(l):
                if nums[i]>nums[j]:
                    p+=1
            arr.append(p)
        return arr
                    