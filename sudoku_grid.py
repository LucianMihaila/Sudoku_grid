def row_correct(sudoku:list,row_no:int):
    linie=sudoku[row_no]
    lista=set()
    for element in range(0,9):
        if linie[element] in lista:
            return False
        if linie[element]!=0:
            lista.add(linie[element])
    return True

def column_correct(sudoku:list,column_no:int):
    lista=set()
    for i in range(0,9):
        if sudoku[i][column_no] in lista:
            return False
        if sudoku[i][column_no]!=0:
            lista.add(sudoku[i][column_no])
    return True

def block_correct(sudoku:list,row_no:int,column_no:int):
    lista=set()

    for linie in range(0,3):
        for coloana in range(0,3):
            poz=sudoku[linie+row_no][coloana+column_no]
            if poz in lista:
                return False
            if poz!=0:
                lista.add(poz)
    return True

def sudoku_grid_correct(sudoku:list):
    for i in range(0,9):
        for j in range(0,9):
            if not row_correct(sudoku,i):
               return False
            if not column_correct(sudoku,j):
                return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not block_correct(sudoku,i,j):
                return False
    return True
            
if __name__=="__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
