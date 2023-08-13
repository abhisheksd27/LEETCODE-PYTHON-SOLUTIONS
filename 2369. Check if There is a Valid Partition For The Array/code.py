class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        
        def fn(i,n):
            if i in dp:
                return dp[i]
            if n == 0:
                return True
            if n<2:
                return False
            x = False
            if nums[i]==nums[i+1]:
                x = fn(i+2,n-2)
            if n>2:
                if nums[i]==nums[i+1] and nums[i+1]==nums[i+2]:
                    if x==False:
                        x = fn(i+3,n-3)
                if nums[i+1]-nums[i] == 1 and nums[i+2]-nums[i+1] == 1:
                    if x==False:
                        x = fn(i+3,n-3)
            dp[i] = x
            return x
        n = len(nums)
        return fn(0,n)