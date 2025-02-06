class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        found = False

        top = 0
        bottom = rows - 1

        while (top<=bottom ):

            middle = (top + bottom) // 2

            if  matrix[middle][0] <= target and matrix[middle][-1] >= target:
                return self.binarySearch(matrix[middle],target)

            elif matrix[middle][0] > target :
                 bottom = middle -1 

            elif matrix[middle][-1] < target:
                 top = middle + 1


        return False

    def binarySearch(self,row: List[int],target: int) -> bool:
        left = 0 
        right = len(row) -1
        found = False
        while (left<=right):
            middle = (left+right)//2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                left = middle + 1 
            else:
                right = middle - 1 

        return found            

