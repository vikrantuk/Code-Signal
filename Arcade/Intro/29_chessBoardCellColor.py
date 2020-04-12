'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.

'''

def chessBoardCellColor(cell1, cell2):
    di = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    c1x=di[cell1[0]]
    c1y = int(cell1[1])
    c2x= di[cell2[0]]
    c2y=int(cell2[1])
    
    if((c1x+c2x+c1y+c2y)%2==1):
        return False
    return True
