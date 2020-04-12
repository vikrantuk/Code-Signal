'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''

def minesweeper(matrix):
    res=[]
    for i in range(len(matrix)):
        res.append(list())
        for j in range(len(matrix[0])):
            res[i].append(0)
    print(res)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j+1<len(matrix[0]) and matrix[i][j+1]==True):
                res[i][j]+=1
            if(i+1<len(matrix) and matrix[i+1][j]==True):
                res[i][j]+=1
            if(j+1<len(matrix[0]) and i+1<len(matrix) and matrix[i+1][j+1]==True):
                res[i][j]+=1
            if(j-1>=0 and matrix[i][j-1]==True):
                res[i][j]+=1
            if(i-1>=0 and matrix[i-1][j]==True):
                res[i][j]+=1
            if(j-1>=0 and i-1>=0 and matrix[i-1][j-1]==True):
                res[i][j]+=1
            if(j+1<len(matrix[0]) and i-1>=0 and matrix[i-1][j+1]==True):
                res[i][j]+=1
            if(i+1<len(matrix) and j-1>=0 and matrix[i+1][j-1]==True):
                res[i][j]+=1
    return(res)
