class Solution:
    def search(self, arr, target):
        head = 0
        tail = len(arr) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        rowhead = 0
        rowtail = len(matrix) - 1
        while rowhead <= rowtail:
            rmid = (rowhead + rowtail) // 2
            if matrix[rmid][0] <= target <= matrix[rmid][-1]:
                return self.search(matrix[rmid], target)
            elif matrix[rmid][0] > target:
                rowtail = rmid - 1
            else:
                rowhead = rmid + 1
        return False
