class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0

        for i in range(m):
            is_sorted = True
            for j in range(1, n):
                if ord(strs[j][i]) < ord(strs[j - 1][i]):
                    is_sorted = False
                    break

            if not is_sorted:
                count += 1

        return count