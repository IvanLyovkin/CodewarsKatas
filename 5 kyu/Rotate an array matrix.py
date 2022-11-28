def rotate(matrix, direction):
    N = len(matrix)
    M = len(matrix[0])
    
    if direction == "clockwise":
        return [[matrix[i][j] for i in range(N-1, -1, -1)] for j in range(0, M)]        
    else:
        return [[matrix[i][j] for i in range(0, N)] for j in range(M-1, -1, -1)]