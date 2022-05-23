matrix = [el.split() for el in input().split("|")]
matrix.reverse()

flat = [el for row in range(len(matrix)) for el in matrix[row]]
print(' '.join(flat))