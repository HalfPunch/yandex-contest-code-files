from sys import exit

input_list = input().split(' ')
rows, columns = [int(input_list[i]) for i in (0, 1)]
if rows > columns:
    rows, columns = columns, rows
if rows == 1:
    if (columns - 1) % 3 == 0:
        print(columns)
    else:
        print(columns//3)
    exit(0)
if rows * columns <= 4:
    print(rows * columns)
    exit(0)
columns_with_liers = (columns + 1)//2 + (columns + 1) % 2
if columns_with_liers % 2 == 0:
    print(columns_with_liers // 2 * rows)
    exit(0)
print(columns_with_liers // 2 * (rows - 1) + rows // 2)
