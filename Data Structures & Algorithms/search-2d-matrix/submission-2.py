class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l = 0
            r = int(len(matrix[i])) - 1
            if target >= matrix[i][l] and target <= matrix[i][r]:
                if target in matrix[i]:
                    return True
                else:
                    return False
        
        return False