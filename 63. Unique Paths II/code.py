class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        if n==1 and m==1:
            return 1 if matrix[0][0]==0 else 0
        flag=1
        if matrix[0][0]==1:
            return 0
        for i in range(1,m):
            if matrix[i][0]==1:
                flag=-1
            matrix[i][0]=flag
        flag=1
        for i in range(1,n):
            if matrix[0][i]==1:
                flag=-1
            matrix[0][i]=flag
        for i in range(n+1,n*m):
            row=i//n
            col=i%n
            if row==0 or col==0:
                continue
            if matrix[row][col]==1:
                matrix[row][col]=-1
            if matrix[row][col]==-1:
                continue
            else:
                if matrix[row-1][col]==-1 and matrix[row][col-1]==-1:
                    matrix[row][col]=-1
                elif matrix[row-1][col]==-1:
                    matrix[row][col]=matrix[row][col-1]
                elif matrix[row][col-1]==-1:
                    matrix[row][col]=matrix[row-1][col]
                else:
                    matrix[row][col]=matrix[row-1][col]+matrix[row][col-1]
        return matrix[m-1][n-1] if matrix[m-1][n-1]!=-1 else 0