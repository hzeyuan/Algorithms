'''
在一个二维整数中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维层叠和一个整数，判断数组中是否包含该整数。
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 找到右上角的数字，从右上角的数字出发,>target，左移，<target 下移
        m = len(matrix)
        # 列表为空的情况
        if  m==0:
            return False
        n = len(matrix[0])
        # 列表中的列表为空的情况
        if n == 0:
            return False
        # 目标数大于右下角的数字时，或者目标数小于左上角的数字时
        if target >matrix[m-1][n-1] or target< matrix[0][0]:
            return False
        x, y = 0, n - 1 # x为行数，y为列数
        number = matrix[x][y] # 右上角的元素
        # 判断矩阵中的元素
        while 0<=x<m and 0<=y<n:
            number = matrix[x][y]
            if target >number:
                x +=1
            elif target <number:
                y -=1
            else:
                return True
        return False



s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
,20))
