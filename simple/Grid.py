class Grid:
    row_num=6
    col_num=6
    def __init__(self):
        self.row_num=Grid.row_num
        self.col_num=Grid.col_num
        self.cells = []

        for i in range(Grid.row_num):
            self.cells.append([0 for i in range(Grid.col_num)])

    def printGrid(self):
        for i in range(Grid.row_num):
            print(self.cells[i])
        print("--------------")
