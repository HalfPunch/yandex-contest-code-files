# basically I am supposed to read from sys.stdin
# but for this file(for testing/debug purposes) I read from function params
def main(matrix_size_str: str, matrix_str: list):
    # converting str input into in values
    matrix_size = []
    for item in matrix_size_str.split():
        try:
            matrix_size.append(int(item))
        except ValueError:
            print('I will print it as an incorrect answer')
    if min(matrix_size) <= 0:
        print(0)
        return 0
    # converting str matrix into int values(and an actual matrix)
    matrix = [[0 for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    row = 0
    for line in matrix_str:
        if row >= matrix_size[0]:
            break
        column = 0
        for item in line.split():
            if column >= matrix_size[1]:
                break
            try:
                matrix[row][column] = int(item)
            except ValueError:
                print('I will print it as an incorrect answer')
                return 0
            column += 1
        row += 1
    # creating heatmap to determine maximum value in the bottom right corner
    # try except cases are needed for situation where there is given bigger matrix than matrix_size
    matrix_heatmap = [[0 for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    for row in range(matrix_size[0]):
        try:
            for column in range(matrix_size[1]):
                try:
                    # middle section
                    if row != 0 and column != 0:
                        matrix_heatmap[row][column] = matrix[row][column] + max(matrix_heatmap[row-1][column], matrix_heatmap[row][column-1])
                    # upper row
                    elif row == 0 and column != 0:
                        matrix_heatmap[row][column] = matrix[row][column] + matrix_heatmap[row][column-1]
                    # left-most column
                    elif row != 0 and column == 0:
                        matrix_heatmap[row][column] = matrix[row][column] + matrix_heatmap[row-1][column]
                    # upper left corner
                    else:
                        matrix_heatmap[row][column] = matrix[row][column]
                except IndexError:
                    break
        except IndexError:
            break
    # to determine path we will regressively choose nearest maximum number to the bottom right corner number
    reversed_path = []
    row, column = matrix_size[0] - 1, matrix_size[1] - 1
    while row > 0 and column > 0:
        if matrix_heatmap[row - 1][column] > matrix_heatmap[row][column - 1]:
            row -= 1
            reversed_path.append("D")
        else:
            column -= 1
            reversed_path.append("R")
    if row == 0:
        for i in range(column):
            reversed_path.append("R")
    else:
        for i in range(row):
            reversed_path.append("D")
    '''
    # it's here for debugging purposes
    print("MATRIX")
    for line in matrix:
        print(line)
    print("HEATMAP")
    for line in matrix_heatmap:
        print(line)
    '''
    # our answer is the bottom right number
    print(matrix_heatmap[-1][-1])
    # an actual path will be reversed
    print(" ".join(reversed(reversed_path)))

    return 0


if __name__ == '__main__':
    testing_matrix_mask = [
        "1 1 1 0 0 0 0",
        "0 0 1 0 0 0 0",
        "0 0 1 0 0 0 0",
        "0 0 1 1 0 0 0",
        "0 0 0 1 1 1 0",
        "0 0 0 0 0 1 0",
        "0 0 0 0 0 1 1",
    ]
    for row in range(8):
        for column in range(8):
            print(" NEXT TEST \n")
            main(str(row) + " " + str(column), testing_matrix_mask)
