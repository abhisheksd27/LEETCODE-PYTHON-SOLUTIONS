class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1=str(n)
        product=1
        Sum=0
        for i in range(len(n1)):
            product *=int(n1[i])
            Sum+=int(n1[i])
        return product-Sum



