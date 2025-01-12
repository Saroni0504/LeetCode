class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        for j in range(n):
            if not self.check_diagonal(0, j, matrix):
                return False

        for i in range(1, m):
            if not self.check_diagonal(i, 0, matrix):
                return False
        
        return True

    def check_diagonal(self, i, j, matrix):
        wanted = matrix[i][j]
        while i + 1 < len(matrix) and j + 1 < len(matrix[0]):
            i += 1
            j += 1
            if matrix[i][j] != wanted:
                return False
        return True

