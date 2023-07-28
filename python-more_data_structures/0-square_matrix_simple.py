def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        result_matrix.append(new_row)
    return result_matrix
        
matrix = [
    
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]
if __name__ == "__main__":

 new_matrix = square_matrix_simple(matrix)
 