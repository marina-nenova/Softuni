line_1, line_2, line_3 = input(), input(), input()
line_1 = line_1.replace(' ', '')
line_2 = line_2.replace(' ', '')
line_3 = line_3.replace(' ', '')
column_1 = ''.join([line_1[0], line_2[0], line_3[0]])
column_2 = ''.join([line_1[1], line_2[1], line_3[1]])
column_3 = ''.join([line_1[2], line_2[2], line_3[2]])
diagonal_1 = ''.join([column_1[0], column_2[1], column_3[2]])
diagonal_2 = ''.join([column_1[2], column_2[1], column_3[0]])

board= [line_1, line_2, line_3, column_1, column_2, column_3, diagonal_1, diagonal_2]
if '111' in board:
    print('First player won')
elif '222' in board:
    print('Second player won')
else:
    print('Draw!')