class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for _ in nums2:
            nums1.pop()
        nums1 += nums2
        nums1.sort()