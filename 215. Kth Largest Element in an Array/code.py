class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(1, len(nums)+1):
            i=k
            return nums[-i]

