# Link for the task: https://coderun.yandex.ru/problem/knight-move/description?currentPage=1&pageSize=20&search=
def factorial(rank: int) -> int:
    fact = 1
    for i in range(1, rank+1):
        fact *= i
    return fact


def main():
    row, column = 0, 0
    try:
        row, column = [int(i) for i in input().split()]
        row -= 1
        column -= 1
    except ValueError:
        print("Incorrect input format")
    '''
    3x3 grid will look like:
    1 0 0
    0 0 1
    0 1 0
    Where numbers represent amount of ways for knight to get to the cell
    1. If sum of coordinates(both x and y in [0:inf+)) can not be divided by 3 there is no way for our knight to get here
    2. If x/y > 2.0 or y/x > 2.0 there is no way for our knight to get here
    3. If 1 and 2 in not true then there is a certain amount of ways to get here:
        -> Amount is determined by Newton's binomial formula for coefficients
            -> The pattern can be seen if you draw a large grid
    '''
    if row == 0 and column == 0:
        print(1)
        return 0
    elif row == 0 or column == 0:
        print(0)
        return 0
    elif (((row + column) % 3 != 0
            or row // column > 2
            or column // row > 2)
            or (row // column == 2 and row % column != 0)
            or (column // row == 2 and column % row != 0)):
        print(0)
        return 0
    # for this instance I'll use standard coefficient naming from the formula
    N = (row + column) // 3
    k = (N + 1 - abs(row - column)) // 2
    ways = factorial(N) // (factorial(k) * factorial(N-k))
    print(ways)

if __name__ == '__main__':
    main()
