class Grid:
    def __init__(self, row_num, col_num):
        self.row_num=row_num
        self.col_num=col_num
        self.cells = []

        for i in range(row_num):
            self.cells.append([0 for i in range(col_num)])

    def printGrid(self):
        for i in range(self.row_num):
            print(self.cells[i])
        print("------------")
