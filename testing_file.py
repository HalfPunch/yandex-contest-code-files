import sys


def main():
    heatmap_size_str = input().split()
    heatmap = [[0 for i in range(int(heatmap_size_str[0]))] for i in range(int(heatmap_size_str[1]))]
    row = 0
    for line in sys.stdin.readlines():
        column = 0
        for value in line.split():
            if row != 0 and column != 0:
                heatmap[row][column] = int(value) + max(heatmap[row-1][column],heatmap[row][column-1])
            elif row == 0 and column != 0:
                heatmap[row][column] = int(value) + heatmap[row][column-1]
            elif row != 0 and column == 0:
                heatmap[row][column] = int(value) + heatmap[row-1][column]
            else:
                heatmap[row][column] = int(value)
            column += 1


if __name__ == '__main__':
    main()
