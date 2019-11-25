'''
对称矩阵
[1,2,3]
[2,4,5]
[3,5,6]
'''

matrix = [[1,2,3],
          [2,4,5],
          [3,5,6]]

'''
对角矩阵,下三角
[1,2,3]
[0,4,5]
[0,0,6]
'''
matrix1 = [[1,0,0],
           [2,4,0],
           [3,5,6]]

# 按照公式，存储的一维数组,下三角
def saveArray(matrix):
    size = len(matrix)
    array = [0]*int(size*(size-1)/2+size)
    i = 1 # 行
    for arr in matrix:
        for number in arr:
            j = arr.index(number) +1 # 列
            if i>=j:
                k = int(((i-1)*i)/2+(j-1))
                array[k] = number
        i+=1
    return array

print(saveArray(matrix))
print(saveArray(matrix1))


sparseMatrix = [[1,0,0],
                [0,0,5],
                [3,0,0]]



def savesparseMatrixToArray(matrix):
    # 稀疏矩阵
    sparseMatrix = {
        "arr": [],
        "n": 0,  # 矩阵的行
        "m": 0,  # 矩阵的列
        "num": 0  # 矩阵非0元素的个数
    }
    count =0
    i = 1  # 行
    for arr in matrix:
        for number in arr:
            if number !=0:
                j = arr.index(number) + 1  # 列
                sparseMatrix["arr"].append((number,i,j))
                count +=1
        i += 1
    sparseMatrix["n"] = i
    sparseMatrix["m"] = j
    sparseMatrix["num"] = count
    return sparseMatrix

print(savesparseMatrixToArray(sparseMatrix))
